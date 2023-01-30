from flask import Flask, request, jsonify
import gosnomer
from models import *
from generate_numbers import GenerateNumbres
from sqlalchemy.orm import sessionmaker
from authorization import TokenNumbres


app = Flask(__name__)

Session = sessionmaker(bind=engine)
session = Session()
TOKEN = TokenNumbres.token()


@app.route("/PLATE/GENERATE", methods=["GET"])
def generate_plate():
    token = request.headers.get("Authorization")
    amount = request.args.get("amount")
    if TOKEN != token != None:
        return {"Error": "Указан не верный токен"}, 401

    if token is None:
        return {"Error": "Missing authorization token"}, 401
    if amount is None:
        amount = 1
    else:
        amount = int(amount)

    new_number = {}
    for num in range(amount):
        try:
            new_number[num + 1] = GenerateNumbres.numbers()

        except ValueError as e:
            return jsonify({"Error": str(e)}), 401

    return jsonify(new_number), 201


@app.route("/PLATE/GET", methods=["GET"])
def get_plate():
    token = request.headers.get("Authorization")
    numbers_id = request.args.get("id")
    if TOKEN != token != None:
        return {"Error": "Указан не верный токен"}, 401

    if token is None:
        return {"Error": "Missing authorization token"}, 401

    if id is None:
        return {"Error": "Не указан идентификатор записи о государственном номере"}, 422

    connection = engine.connect()

    number = session.query(Numbers).filter_by(number_id=numbers_id).first()
    if not number:
        return {"Error": "Сожалею но такого номера нет"}, 404

    connection.close()
    return jsonify({str(number.number_id): number.auto_numbers}), 200


@app.route("/PLATE/ADD", methods=["POST"])
def post_plate():
    token = request.headers.get("Authorization")
    plate = request.args.get("plate")

    if TOKEN != token != None:
        return {"Error": "Указан не верный токен"}, 401

    if token is None:
        return {"Error": "Missing authorization token"}, 401

    if plate is None:
        return {"Error": "Укажите государственный номер автомобиля"}, 422

    try:
        number_add = {}
        connection = engine.connect()
        plate = gosnomer.normalize(plate)

        if session.query(Numbers).filter_by(auto_numbers=plate).first() is not None:
            return jsonify({"Error": f"Номер {plate} уже существует"}), 401

        record = Numbers(number_id=uuid.uuid4(), auto_numbers=plate)
        session.add(record)
        session.flush()
        number_add[str(record.number_id)] = record.auto_numbers
        connection.close()
        return jsonify(number_add), 201

    except ValueError as e:
        return {"Error": str(e)}, 401


if __name__ == "__main__":
    app.run()
