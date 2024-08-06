from flask import Flask
from backend.src.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    login.login_view = 'auth.login'
    login.login_message = 'Please log in to access this page.'
    login.login_message_category = 'info'

    from backend.src.auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from backend.src.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
