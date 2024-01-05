from config.dbutil import *

print(app)

# with app.app_context():
#     Base.prepare(db.engine, reflect=True)
#
#     Userinfo = Base.classes.user_info
#
#     all_users = Userinfo.query.all()
#
#     for user in all_users:
#         print(user)
