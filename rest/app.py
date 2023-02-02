import logging
import gosnomer
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from flask import Flask, request, jsonify
from generate_numbers import RegistrationMarkGenerator

from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config

from dotenv import  load_dotenv
registration_mark_generator = RegistrationMarkGenerator()


app = Flask(__name__)
app.config.from_object(Config)
load_dotenv()
url = os.getenv("DATABASE_URL")
engine = create_engine(url)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()
jwt = JWTManager(app)

from models import *
Base.metadata.create_all(bind=engine)




# def setup_logger():
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#
#     formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
#     file_handler = logging.FileHandler('log/api.log')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#
#     return logger
#
# logger = setup_logger()


@app.route("/PLATE/GENERATE", methods=["GET"])
@jwt_required()
def generate_plate():
    amount = request.args.get("amount")
    try:
        amount = 1 if amount is None else int(amount)
        registration_mark = {}
        for num in range(amount):
            registration_mark[num + 1] = registration_mark_generator.generate_car_number()
        return jsonify(registration_mark), 200
    except ValueError as e:
        # logger.warning(f'user:{user_id} tutorials - read acrion failed with errors: {e}')
        return {"Error": str(e)}, 401



@app.route("/PLATE/GET", methods=["GET"])
@jwt_required()
def get_plate():
    try:
        request_registration_mark = request.args.get("id")
        existing_registration_mark = session.query(RegistrationNumbers).filter_by(id=request_registration_mark).first()
        return jsonify({str(existing_registration_mark.id): existing_registration_mark.auto_numbers}), 200
    except ValueError as e:
        return {"Error": str(e)}, 401




@app.route("/PLATE/ADD", methods=["POST"])
@jwt_required()
def post_plate():
    plate = request.args.get("plate")
    try:
        user_id = get_jwt_identity()
        response_registration_mark = {}
        plate = gosnomer.normalize(plate)
        record = RegistrationNumbers(user_id=user_id, id=uuid.uuid4(), auto_numbers=plate)
        session.add(record)
        session.commit()
        response_registration_mark[str(record.id)] = record.auto_numbers
        return jsonify(response_registration_mark), 201
    except ValueError as e:
        return {"Error": str(e)}, 401


@app.route("/PLATE/REGISTER", methods=["POST"])
def register():
    params = request.json
    user = User(**params)
    session.add(user)
    session.commit()
    token = user.get_token()
    return jsonify({'access_token': token})


@app.route("/PLATE/LOGIN", methods=["POST"])
def login():
    params = request.json
    user = User.authenticate(**params)
    token = user.get_token()
    return jsonify({'access_token': token})

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()



# @app.errorhandler
# def error_handler(err):
#     headers = err.data.get('headers', None)
#     messages = err.data.get('messages', ['Invalid request'])
#     if headers:
#         return jsonify({'message': messages}), 400, headers
#     return jsonify({'message': messages}), 400


if __name__ == "__main__":
    app.run()
