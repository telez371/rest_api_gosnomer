import uuid

from marshmallow import Schema, validate, fields


class RegistrationNumbersSchema(Schema):
    id = fields.String(required=True)
    auto_numbers = fields.String(required=True)
    message = fields.String(dump_only=True)


class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    car_numbers = fields.Nested(RegistrationNumbersSchema, many=True, dump_only=True)


class AuthSchema(Schema):
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)


class GenerateSchema(Schema):
    amount = fields.Integer(required=True)


class GenerateNumSchemas(Schema):
    generate_car_numbers = fields.Str()


class UserNumbersSchema(Schema):
    auto_numbers = fields.String(required=True)
