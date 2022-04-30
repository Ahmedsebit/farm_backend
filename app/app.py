from app.utils.exceptions import ResponseError
import json
import logging
import re
import os
from datetime import datetime
from flask_api import FlaskAPI, status
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config
from flask_swagger_ui import get_swaggerui_blueprint
import os

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from flask import jsonify

db = SQLAlchemy()
migrate = Migrate(db)


### swagger specific ###
SWAGGER_URL = '/farm_backend/swagger'
API_URL = '/static/swagger.json'
URL_PREFIX = '/farm_backend/v1'
URL_PREFIX_V2 = '/farm_backend/v2'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "farm_backend"
    }
)
    

logger = logging.getLogger(__name__)


def create_app(config_name):
    '''
    Wraps the creation of a new Flask object, and returns it after it's loaded up
    with configuration settings using app.config and connected to the DB using
    '''
    
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 10
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 120
    app.config['SQLALCHEMY_POOL_PRE_PING'] = True
    app.config['COGNITO_REGION'] = 'eu-central-1'
    app.config['COGNITO_USERPOOL_ID'] = 'eu-central-1c3fea2'
    app.config['COGNITO_APP_CLIENT_ID'] = 'abcdef123456'  # client ID you wish to verify user is authenticated against
    app.config['COGNITO_CHECK_TOKEN_EXPIRATION'] = False  # disable token expiration checking for testing purposes
    app.config['COGNITO_JWT_HEADER_NAME'] = 'X-MyApp-Authorization'
    app.config['COGNITO_JWT_HEADER_PREFIX'] = 'Bearer'
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_IDENTITY_CLAIM'] = 'jti'
    
    jwt = JWTManager(app)
    
    migrate.init_app(app, db)
    
    app.app_context().push()
    log_level = logging.INFO
    app.logger.setLevel(log_level)
    
    import app.api.v1.views as api_v1
    
    db.init_app(app)
    
    app.register_blueprint(api_v1.farm_backend_v1_api_bp, url_prefix=URL_PREFIX)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    # @app.errorhandler(Exception)
    # def handle_error(e):
    #     logger.error(f"Transporter Management - {type(e).__name__}: {str(e)}")

    #     if isinstance(e, ResponseError):
    #         return jsonify(**e.__dict__), e.status

    #     return jsonify(dict(detail=f"{type(e).__name__}: {str(e)}")), 500
    
    @app.teardown_request
    def teardown_request(exception):
        if exception:
            db.session.rollback()
        db.session.remove()

    return app
