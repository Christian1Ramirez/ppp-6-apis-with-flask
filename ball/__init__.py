from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:03040506aS!@localhost:5432/ballpy"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def index():
        return "Hello, Flask Application Factory!"

    from .reptile import reptile_bp
    app.register_blueprint(reptile_bp)
    return app
