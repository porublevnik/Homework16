from init_db import db
from models import User, Offer, Order
from flask import Flask, jsonify, request, abort
from migrate import data_to_db

app = Flask(__name__)


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        try:
            users = db.session.query(User).all()
            return jsonify([user.serialize() for user in users])
        except Exception as e:
            return f'{e}'

    elif request.method == 'POST':
        data = request.json
        db.session.add(User(**data))
        db.session.commit()
        return jsonify(code=200)


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        user = db.session.query(User).get(user_id)
        if user is None:
            return 'User not found', 404
        return jsonify(user.serialize())

    elif request.method == 'PUT':
        user = db.session.query(User).filter(User.id == user_id)
        if user is None:
            return 'User not found', 404
        user.update(request.json)
        db.session.commit()
        return jsonify(code=200)

    elif request.method == 'DELETE':
        user = db.session.query(User).get(user_id)
        if not user:
            return 'User not found', 404
        db.session.delete(user)
        db.session.commit()
        return jsonify(code=200)


@app.route('/orders/', methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        try:
            orders = db.session.query(Order).all()
            return jsonify([order.serialize() for order in orders])
        except Exception as e:
            return f'{e}'

    elif request.method == 'POST':
        data = request.json
        db.session.add(Order(**data))
        db.session.commit()
        return jsonify(code=200)


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(order_id):
    if request.method == 'GET':
        order = db.session.query(Order).get(order_id)
        if order is None:
            return 'Order not found', 404
        return jsonify(order.serialize())

    elif request.method == 'PUT':
        order = db.session.query(Order).filter(Order.id == order_id)
        if order is None:
            return 'Order not found', 404
        order.update(request.json)
        db.session.commit()
        return jsonify(code=200)

    elif request.method == 'DELETE':
        order = db.session.query(Order).get(order_id)
        if order is None:
            return 'Order not found', 404
        db.session.delete(order)
        db.session.commit()
        return jsonify(code=200)


@app.route('/offers/', methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        try:
            offers = db.session.query(Offer).all()
            return jsonify([offer.serialize() for offer in offers])
        except Exception as e:
            return f'{e}'

    elif request.method == 'POST':
        data = request.json
        db.session.add(Offer(**data))
        db.session.commit()
        return jsonify(code=200)


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(offer_id):
    if request.method == 'GET':
        offer = db.session.query(Offer).get(offer_id)
        if offer is None:
            return 'Offer not found', 404
        return jsonify(offer.serialize())

    elif request.method == 'PUT':
        offer = db.session.query(Offer).filter(Offer.id == offer_id)
        if offer is None:
            return 'Offer not found', 404
        offer.update(request.json)
        db.session.commit()
        return jsonify(code=200)
    elif request.method == 'DELETE':
        offer = db.session.query(Offer).get(offer_id)
        if offer is None:
            return 'Offer not found', 404
        db.session.delete(offer)
        db.session.commit()
        return jsonify(code=200)


if __name__ == '__main__':
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        data_to_db()

    app.run(port=8000)