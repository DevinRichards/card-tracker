import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

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

    from . import routes, auth
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')

    return app

@login.user_loader
def load_user(user_id):
    from .models import User  # Import here to avoid circular dependency
    return User.query.get(int(user_id))
