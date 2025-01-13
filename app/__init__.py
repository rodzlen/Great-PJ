from config import db
from flask import Flask
from flask_migrate import Migrate
from app.routes import question_blp,user_blp

migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)
    with application.app_context():
        db.create_all()
    migrate.init_app(application, db)

    application.register_blueprint(question_blp)
    application.register_blueprint(user_blp)
    # 블루 프린트 등록

    return application
