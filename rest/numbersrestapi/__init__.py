import logging
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from flask import Flask, request, current_app
from .generate_numbers import RegistrationMarkGenerator
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_jwt_extended import JWTManager
from .config import Config
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from dotenv import load_dotenv

registration_mark_generator = RegistrationMarkGenerator()

app = Flask(__name__)
app.config.from_object(Config)
load_dotenv()
url = os.getenv("DATABASE_URL")
engine = create_engine(url)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()
jwt = JWTManager()
docs = FlaskApiSpec()

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='numbersrestapi',
        version='1.0',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()], ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})

Base.metadata.create_all(bind=engine)


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('../rest/log/api.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


from rest.numbersrestapi.main.views import plate_numbers
from rest.numbersrestapi.users.views import users

app.register_blueprint(plate_numbers)
app.register_blueprint(users)
docs.init_app(app)
jwt.init_app(app)
