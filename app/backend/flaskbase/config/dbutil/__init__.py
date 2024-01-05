from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

from config import app

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
    Base = automap_base()
    Base.prepare(db.engine)

    User = Base.classes.statistics

    for user in User:
        print(user)
