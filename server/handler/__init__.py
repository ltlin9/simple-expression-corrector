from .user import UserRegister, UserLogin
from .upload import Upload
from flask import Flask
from flask_restful import Api


def RegisterRoute(app: Flask):
    # app.register_blueprint(user_bp, url_prefix='/user')
    # app.register_blueprint(judge_bp, url_prefix='/judge')
    # app.register_blueprint(upload_bp, url_prefix='/upload')
    api = Api(app)
    # upload
    api.add_resource(Upload, '/upload')
    # user
    api.add_resource(UserRegister, '/user/register')
    api.add_resource(UserLogin, '/user/login')
