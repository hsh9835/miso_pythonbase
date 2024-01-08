# app.py

from flask import Flask
from flask_cors import CORS

from config.plugins.blueprint_autoset import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 데이터베이스 연결 문자열 설정 (your_database_url은 실제 데이터베이스 URL로 대체되어야 합니다)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ta.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 경고 방지용 설정

register_blueprints(app)


@app.route('/', methods=['POST'])
def postReq():
    # POST 요청을 처리하는 코드
    return 'POST 요청이 성공적으로 처리되었습니다.'


@app.route('/axiosTest', methods=['POST'])
def axiosTest():
    return 'axios 작동 잘 되고 있습니다.'


if __name__ == '__main__':
    app.run(debug=True)
