from flask import Flask, jsonify, Blueprint, request, abort

signup = Blueprint('signup', __name__)

test_list = [{"user1": "1234", "user2": "5678"}]


# GETの実装
# curl -i http://0.0.0.0:3001/get
@signup.route('/get', methods=['GET'])
def get():
    result = {"greeting": 'hello flask'}
    return jsonify(result)


# curl -i -X POST -H "Content-Type: application/json" -d '{"username":"miguel","password":"python"}' http://0.0.0.0:3001/signup
@signup.route('/signup', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if username in test_list[0]:
        abort(400) # existing user
    user = username
    # user.hash_password(password)
    # db.session.add(user)
    # db.session.commit()
    return jsonify({ 'username': user }), 201#, {'Location': url_for('get_user', id = user.id, _external = True)}