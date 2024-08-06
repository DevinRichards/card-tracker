from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
from .models import User  
from . import routes, auth 
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')

    return app

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
