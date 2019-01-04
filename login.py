from flask import jsonify, Blueprint

login = Blueprint('login', __name__)


# GETの実装
# curl -i http://0.0.0.0:3001/get
@login.route('/test', methods=['GET'])
def get():
    result = {"test": 'login'}
    return jsonify(result)


