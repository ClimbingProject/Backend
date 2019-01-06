from flask import jsonify, Blueprint, request, abort
import boto3
from botocore.exceptions import ClientError


login = Blueprint('login', __name__)

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('Users')

# GETの実装
# curl -i -X GET -H "Content-Type: application/json" -d '{"email":"miguel@gmail.com","password":"python"}' http://0.0.0.0:3001/login
@login.route('/login', methods=['GET'])
def get():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        abort(400)  # missing arguments

    try:
        response = table.get_item(Key={"email": email})
        if response['Item']['password'] == password:
            return jsonify({'ok': email + ': successfully logged in.'}), 201
        else:
            abort(400)
    except ClientError as e:
        print(e.response['Error']['Message'])


