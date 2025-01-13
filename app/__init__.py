from config import db
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from app.routes.admin_routes import question_blp_admin,user_blp_admin,image_blp_admin,answer_blp_admin,choice_blp_admin
from app.routes.user_routes import question_blp,user_blp,choice_blp,answer_blp,image_blp

migrate = Migrate()



def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    # openapi
    application.config["API_TITLE"] = "My API"
    application.config["API_VERSION"] = "v1"
    application.config["OPENAPI_VERSION"] = "3.1.3"
    application.config["OPENAPI_URL_PREFIX"] = "/"
    application.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    application.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(application)

    db.init_app(application)
    with application.app_context():
        db.create_all()
    migrate.init_app(application, db)

    # 블루 프린트 등록
    # admin
    # application.register_blueprint(choice_blp_admin)
    # application.register_blueprint(question_blp_admin)
    # application.register_blueprint(user_blp_admin)
    # application.register_blueprint(image_blp_admin)
    # application.register_blueprint(answer_blp_admin)
    
    # # user
    # application.register_blueprint(choice_blp)
    # application.register_blueprint(question_blp)
    # application.register_blueprint(user_blp)
    # application.register_blueprint(image_blp)
    # application.register_blueprint(answer_blp)

    #openapi 블루프린트
    # admin
    api.register_blueprint(choice_blp_admin)
    api.register_blueprint(question_blp_admin)
    api.register_blueprint(user_blp_admin)
    api.register_blueprint(image_blp_admin)
    api.register_blueprint(answer_blp_admin)
    
    # user
    api.register_blueprint(choice_blp)
    api.register_blueprint(question_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(image_blp)
    api.register_blueprint(answer_blp)


    return application
