from flask import Flask, jsonify, Blueprint, request, abort, send_file
import boto3
import localstack_client.session
from pymongo import MongoClient
from time import gmtime, strftime
import uuid

# TODO change mongoDB url when deploy
client = MongoClient('mongodb://cp:climbing_project1@ds157574.mlab.com:57574/climbing_project')
db = client['climbing_project']

video = Blueprint('video', __name__)


# curl -i -X POST -H "Content-Type: application/json" -d '{"file_name": "zorro.mp4", "user_uuid": "08be0c6b58e64f309b497e9e650b3db4", "place": "", "project_name": "", "difficulty": ""}' http://0.0.0.0:3001/video/upload
@video.route('/video/upload', methods=['POST'])
def get_video():
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
                'ACL': 'public-read', 'ContentType': 'video/mp4'}
        )

        s3.put_object_acl(
            Bucket='cp_s3',  # TODO change bucket name
            Key='{}/{}'.format(user_uuid, file_name),
            GrantRead='uri=http://acs.amazonaws.com/groups/global/AllUsers'
        )

        # upload video to 'videos' table in database
        url = 'http://localhost:4572/cp_s3/' + user_uuid + '/' + file_name  # TODO change this url when deploy
        videos = db['videos']
        videos.insert({
            'likes': 0,
            'user_uuid': user_uuid,
            'time': strftime("%Y-%m-%d %H:%M", gmtime()),
            'place': request.json.get('place'),
            'url': url,
            'project_name': request.json.get('project_name'),
            'difficulty': request.json.get('difficulty'),
        })

        # add video id to user's video list
        # find the user by user's uuid and insert video url
        db['users'].update_one(
            {"uuid": user_uuid},
            {'$addToSet': {'video_list': [url]}}
        )

        return jsonify({'ok': file_name}), 201

    except Exception as e:
        print(e)
        return 'ERROR\n', 400
