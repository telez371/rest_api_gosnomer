from sqlalchemy.ext.mutable import MutableDict
import gosnomer
from . import db, session, Base
from sqlalchemy import Column, String, Integer, UniqueConstraint, create_engine, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import bcrypt


class RegistrationNumbers(Base):
    __tablename__ = 'user_my_car_numbers'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    users_id = db.Column(db.Integer, db.ForeignKey('numbers_user_base.id'))
    auto_numbers = db.Column(db.String, primary_key=True, unique=True)

    @classmethod
    def get_user_list(csl, numbers_id, ):
        try:
            numbers_id = csl.query.filter_by(id=numbers_id).first()
            if not numbers_id:
                raise Exception('No numbers')
        except Exception:
            session.rollback()
            raise
        return numbers_id

    @classmethod
    def post_plate_add(cls, plate):
        try:
            new_plate = gosnomer.normalize(plate)
            search_numbers = cls.query.filter_by(auto_numbers=new_plate).first()
            if search_numbers is not None:
                raise Exception(f"Номер {new_plate} уже существует")

            new_numbers = RegistrationNumbers(auto_numbers=new_plate)
            session.add(new_numbers)
            session.commit()
        except Exception:
            session.rollback()
            raise
        return new_numbers


class User(Base):
    __tablename__ = 'numbers_user_base'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    car_numbers = relationship('RegistrationNumbers', backref='user', lazy=True)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = bcrypt.hash(kwargs.get('password'))

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta)
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).first()
        if not user:
            raise Exception('No user with this email')
        if not bcrypt.verify(password, user.password):
            raise Exception('No user with this password')
        return user


class RandomNumbers(Base):
    __tablename__ = 'randon_numb'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    random_numbers = db.Column(String, nullable=False)


class Generate:
    def __init__(self, generate_car_numbers):
        self.generate_car_numbers = generate_car_numbers

    def __repr__(self):
        return "<Users(generate_car_numbers={self.generate_car_numbers!r})>".format(self=self)
