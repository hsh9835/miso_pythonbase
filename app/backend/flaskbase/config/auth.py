# from flask import Blueprint, request
# from flask_login import LoginManager, UserMixin
#
#
#
# auth = Blueprint('auth', __name__, url_prefix='/auth')
#
# login_manager = LoginManager()
# login_manager.init_app(auth)
#
# class User(UserMixin):
#
#     def __init__(self, user_id):
#         self.user_id = user_id
#
#     def get_id(self):
#         return str(self.user_id)
#
#     # @staticmethod
#     # def get_user_info(user_id, user_pw=None):
#
#
# @login_manager.user
#
# @auth.route('/login', method=['POST'])
# def login():
#
#
# @auth.route('/logout')
# def logout():
#     return None
