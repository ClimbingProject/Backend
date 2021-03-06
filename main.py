from signup import signup
from login import login
from feed import feed
from projects import projects
from delete import delete
import all_module as am

# Flaskクラスのインスタンスを作成
# __name__は現在のファイルのモジュール名
# Register api routes from each files
api = am.Flask(__name__)
api.register_blueprint(signup)
api.register_blueprint(login)
api.register_blueprint(feed)
api.register_blueprint(projects)
api.register_blueprint(delete)


# エラーハンドリング
@signup.errorhandler(404)
def not_found(error):
    return am.jsonify({'error': 'Not found'}), 404


# ファイルをスクリプトとして実行した際に
# ホスト0.0.0.0, ポート3001番でサーバーを起動
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3001, debug=True)