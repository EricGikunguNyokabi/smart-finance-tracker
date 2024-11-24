from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # type: ignore
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)  # Move this inside create_app

    # Set the login view
    login_manager.login_view = 'auth.login'  # Replace 'auth.login' with your login endpoint

    # User loader function
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Import User model here to avoid circular imports
        return User.query.get(int(user_id))

    # Register blueprints
    from app.views import main_bp
    from app.views.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    return app