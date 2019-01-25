import all_module as am

client = am.MongoClient('mongodb://cp:climbing_project1@ds157574.mlab.com:57574/climbing_project')
db = client['climbing_project']

delete = am.Blueprint('delete', __name__)


# curl -i -X POST -H "Content-Type: application/json" -d '{"uuid":"<>"}' http://0.0.0.0:3001/delete/user
@delete.route('/delete/user', methods=['POST'])
def delete_user():
    uuid = am.request.json.get('uuid')
    users = db['users']
    found_user = users.find_one({'uuid': uuid})

    if found_user:
        users.remove({'uuid': uuid})
        return am.jsonify({'ok': uuid + ': successfully deleted.'}), 201

    return 'User, ' + uuid + ' does not exist\n', 400


# curl -i -X POST -H "Content-Type: application/json" -d '{"uuid":"<>"}' http://0.0.0.0:3001/delete/feed
@delete.route('/delete/feed', methods=['POST'])
def delete_user():
    uuid = am.request.json.get('uuid')
    feeds = db['feed']
    found_feed = feeds.find_one({'uuid': uuid})

    if found_feed:
        feeds.remove({'uuid': uuid})
        return am.jsonify({'ok': uuid + ': successfully deleted.'}), 201

    return 'Feed, ' + uuid + ' does not exist\n', 400