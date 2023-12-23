from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app_package import route, models

#from app.models import User, Post
#app.app_context().push()
#u = User()
#u.username = 'admin'
#u.email = 'ztejd@example.com'
#u.password_hash = 'admin'
#db.session.add(u)
#db.session.commit()
#u = db.session.get(User, 1)
#p = Post()
#p.body = 'my first post!'
#p.author = u
#db.session.add(p)
#db.session.commit()