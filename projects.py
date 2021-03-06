import all_module as am

projects = am.Blueprint('projects', __name__)

# TODO change mongoDB url when deploy
client = am.MongoClient('mongodb://cp:climbing_project1@ds157574.mlab.com:57574/climbing_project')
db = client['climbing_project']


# curl -i -X POST -H "Content-Type: application/json" -d '{"name":"Zorro","type":"Boulder", "rating": "V4",
# "location": "[
#                 "California",
#                 "Yosemite National Park",
#                 "Yosemite Valley",
#                 "Yosemite Valley Bouldering",
#                 "Curry Village",
#                 "Zorro Boulder"
#             ]", "long": -119.576, "lag": 37.7375}' http://0.0.0.0:3001/projects/add
@projects.route('/projects/add', methods=['POST'])
def add_project():
    p_name = am.request.json.get('name')
    projects_db = db['projects']
    existed_project = projects_db.find_one({'name': p_name})

    if existed_project is None:
        projects_db.insert({
            'name': p_name,
            'type': am.request.json.get('type'),
            'rating': am.request.json.get('rating'),
            'location': am.request.json.get('location'),
            'longitude': am.request.json.get('long'),
            'latitude': am.request.json.get('lat')
        })
        return am.jsonify({'ok': p_name}), 201

    return 'Project already exist\n', 400


# curl -i -X GET -H "Content-Type: application/json" -d '{"name":"Zorro"}' http://0.0.0.0:3001/projects/get
@projects.route('/projects/get', methods=['GET'])
def get_project():
    p_name = am.request.json.get('name')
    projects_db = db['projects']
    existed_project = projects_db.find_one({'name': p_name})

    if existed_project:
        return am.jsonify({'ok': p_name + ': successfully found.',
                        'content' : existed_project}), 201

    return 'Project, ' + p_name + ' not found\n', 400
