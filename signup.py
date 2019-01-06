from flask import Flask, jsonify, Blueprint, request, abort
import boto3
from botocore.exceptions import ClientError

signup = Blueprint('signup', __name__)

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('Users')

# GETの実装
# curl -i http://0.0.0.0:3001/get
@signup.route('/get', methods=['GET'])
def get():
    result = {"greeting": 'hello flask'}
    return jsonify(result)


# curl -i -X POST -H "Content-Type: application/json" -d '{"email":"miguel@gmail.com","password":"python"}' http://0.0.0.0:3001/signup
@signup.route('/signup', methods=['POST'])
def new_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        abort(400) # missing arguments

    try:
        response = table.get_item(Key={"email": email})#, "password": password})
        print(response)
        if 'Item' in response:
            abort(400) # existing user
        table.put_item(
            Item={
                'email': email,
                'password': password
            }
        )
        # user.hash_password(password)
        # db.session.add(user)
        # db.session.commit()
        return jsonify({ 'ok': email }), 201#, {'Location': url_for('get_user', id = user.id, _external = True)}
    except ClientError as e:
        print(e.response['Error']['Message'])


#"{\"email\":{\"S\": \"miguel@gmail.com\"}}"