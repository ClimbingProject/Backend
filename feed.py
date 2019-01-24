from flask import Flask, jsonify, Blueprint, request, abort, send_file
import boto3
import localstack_client.session
from pymongo import MongoClient
from time import gmtime, strftime
import uuid
from bson.json_util import dumps

# TODO change mongoDB url when deploy
client = MongoClient('mongodb://cp:climbing_project1@ds157574.mlab.com:57574/climbing_project')
db = client['climbing_project']

feed = Blueprint('feed', __name__)


# curl -i -X POST -H "Content-Type: application/json" -d '{"file_name": "zorro.mp4", "user_uuid": "967f6956fbb74f358e7fc894f7db7e10", "place": "", "project_name": "", "difficulty": ""}' http://0.0.0.0:3001/feed/upload
@feed.route('/feed/upload', methods=['POST'])
def upload_video():
    try:
        session = localstack_client.session.Session()
        # TODO s3 = boto3.client('s3') <- Change to this when deploy.
        s3 = session.client('s3')  # this is for local development purpose only

        user_uuid = request.json.get('user_uuid')
        # file_name = '{}.{}'.format(uuid.uuid4().hex, 'mp4')
        file_name = request.json.get('file_name')
        s3.upload_file(
            Filename=file_name,
            Bucket='cp_s3',  # TODO change bucket name
            Key='{}/{}'.format(user_uuid, file_name),
            ExtraArgs={
                'GrantRead': 'uri=http://acs.amazonaws.com/groups/global/AllUsers',
                'ACL': 'public-read', 'ContentType': 'feed/mp4'}
        )

        s3.put_object_acl(
            Bucket='cp_s3',  # TODO change bucket name
            Key='{}/{}'.format(user_uuid, file_name),
            GrantRead='uri=http://acs.amazonaws.com/groups/global/AllUsers'
        )

        # upload feed to 'feed' table in database
        url = 'http://localhost:4572/cp_s3/' + user_uuid + '/' + file_name  # TODO change this url when deploy
        feeds = db['feed']
        feeds.insert({
            'likes': 0,
            'user_uuid': user_uuid,
            'time': strftime("%Y-%m-%d %H:%M", gmtime()),
            'place': request.json.get('place'),
            'url': url,
            'project_name': request.json.get('project_name'),
            'difficulty': request.json.get('difficulty'),
            'uuid': uuid.uuid4().hex
        })

        # add feed id to user's feed list
        # find the user by user's uuid and insert feed url
        db['users'].update_one(
            {"uuid": user_uuid},
            {'$addToSet': {'video_list': [url]}}  # TODO here might need to change to set to list 'addtolist'
        )

        return jsonify({'ok': file_name}), 201

    except Exception as e:
        print(e)
        return 'ERROR\n', 400


# curl -i -X GET -H "Content-Type: application/json" -d '{"n":1}' http://0.0.0.0:3001/feed/n_latest
@feed.route('/feed/n_latest', methods=['GET'])
def n_latest():
    n = request.json.get('n')
    result = db['feed'].find().sort([('$natural', -1)]).limit(n)
    urls = []
    for x in result:
        print(x)
        urls.append(x['url'])
    return jsonify(urls), 201


# curl -i -X POST -H "Content-Type: application/json" -d '{"uuid": "967f6956fbb74f358e7fc894f7db7e10"}' http://0.0.0.0:3001/feed/incre_like
@feed.route('/feed/incre_like', methods=['POST'])
def incre_like():
    db['feed'].items.update({'uuid': request.json.get('uuid')}, { '$inc': {'likes': 1}})
    return jsonify({'ok': 'successfully incremented'}), 201
