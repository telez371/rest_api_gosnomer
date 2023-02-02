from app import db, session, Base
from sqlalchemy import Column, String, Integer, UniqueConstraint, create_engine, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import bcrypt



class RegistrationNumbers(Base):
    __tablename__ = 'my_car_numbers'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    users_id = db.Column(db.Integer, db.ForeignKey('new_users_base.id'))
    auto_numbers = db.Column(db.String, unique=True)



class User(Base):
    __tablename__ = 'new_users_base'
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





