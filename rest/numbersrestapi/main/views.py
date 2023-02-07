from flask import Blueprint
from rest.numbersrestapi import logger, docs, registration_mark_generator
from rest.numbersrestapi.schemas import GenerateSchema, GenerateNumSchemas, RegistrationNumbersSchema
from flask_apispec import marshal_with, use_kwargs
from rest.numbersrestapi.models import RegistrationNumbers, Generate
from flask_jwt_extended import jwt_required, get_jwt_identity

plate_numbers = Blueprint('plate_numbers', __name__)


@plate_numbers.route("/PLATE/GENERATE", methods=["GET"])
@jwt_required()
@use_kwargs(GenerateSchema(only=['amount']))
@marshal_with(GenerateNumSchemas)
def generate_plate(**kwargs):
    try:
        amount = 1 if kwargs.get('amount') == 0 else int(kwargs.get('amount'))
        registration_mark = [{num + 1: registration_mark_generator.generate_car_number() for num in range(amount)}]
        user = Generate(generate_car_numbers=registration_mark)
        schema = GenerateNumSchemas()
        result = schema.dump(user)
    except Exception as e:
        logger.warning(f'user:{get_jwt_identity()} Generate - read action failed with errors: {e}')
        return {"message": str(e)}, 401
    return result


@plate_numbers.route("/PLATE/GET", methods=["GET"])
@jwt_required()
@use_kwargs(RegistrationNumbersSchema(only=['id']))
@marshal_with(RegistrationNumbersSchema(only=["auto_numbers"]))
def get_plate(**kwargs):
    try:
        numbers_id = kwargs.get("id")
        existing_registration_mark = RegistrationNumbers.get_user_list(numbers_id=numbers_id)
    except Exception as e:
        logger.warning(f'user: get_id - read action failed with errors: {e}')
        return {"message": str(e)}, 401

    return existing_registration_mark


@plate_numbers.route("/PLATE/ADD", methods=["POST"])
@jwt_required()
@use_kwargs(RegistrationNumbersSchema(only=['auto_numbers']))
@marshal_with(RegistrationNumbersSchema)
def post_plate(**kwargs):
    try:
        plate = kwargs.get("auto_numbers")
        record = RegistrationNumbers.post_plate_add(plate=plate)
    except Exception as e:
        logger.warning(f'user: Post - read action failed with errors: {e}')
        return {"message": str(e)}, 401
    return record


@plate_numbers.errorhandler(422)
def error_handler(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request'])
    if headers:
        return {'message': messages}, 400, headers
    return {'message': messages}, 400


docs.register(generate_plate, blueprint='plate_numbers')
docs.register(get_plate, blueprint='plate_numbers')
docs.register(post_plate, blueprint='plate_numbers')
