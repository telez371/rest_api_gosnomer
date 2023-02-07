from flask import Blueprint, jsonify
from rest.numbersrestapi import logger, session, docs
from rest.numbersrestapi.schemas import UserSchema, AuthSchema
from flask_apispec import marshal_with, use_kwargs
from rest.numbersrestapi.models import User

users = Blueprint('users', __name__)


@users.route("/PLATE/REGISTER", methods=["POST"])
@use_kwargs(UserSchema)
@marshal_with(AuthSchema)
def register(**kwargs):
    try:
        user = User(**kwargs)
        session.add(user)
        session.commit()
        token = user.get_token()
    except Exception as e:
        logger.warning(f'user: REGISTER - read action failed with errors: {e}')
        return {"Error": str(e)}, 401
    return {'access_token': token}


@users.route("/PLATE/LOGIN", methods=["POST"])
@use_kwargs(UserSchema(only=('email', 'password')))
@marshal_with(AuthSchema)
def login(**kwargs):
    try:
        user = User.authenticate(**kwargs)
        token = user.get_token()
    except Exception as e:
        logger.warning(f'user: LOGIN - read action failed with errors: {e}')
        return {"Error": str(e)}, 401
    return jsonify({'access_token': token})


@users.errorhandler(422)
def error_handler(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request'])
    if headers:
        return {'message': messages}, 400, headers
    return {'message': messages}, 400


docs.register(register, blueprint='users')
docs.register(login, blueprint='users')
