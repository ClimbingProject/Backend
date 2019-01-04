from flask import Flask, jsonify, Blueprint

signup = Blueprint('signup', __name__)


# GETの実装
# curl -i http://0.0.0.0:3001/get
@signup.route('/get', methods=['GET'])
def get():
    result = {"greeting": 'hello flask'}
    return jsonify(result)
