from flask import Blueprint, request, jsonify
from .models import db, User, Card

bp = Blueprint('main', __name__)

@bp.route('/cards', methods=['GET', 'POST'])
def manage_cards():
    if request.method == 'POST':
        data = request.get_json()
        card = Card(
            name=data['name'],
            set=data['set'],
            price=data.get('price', 0),
            alert_price=data.get('alert_price', None),
            user_id=data['user_id']
        )
        db.session.add(card)
        db.session.commit()
        return jsonify({'message': 'Card added'}), 201

    cards = Card.query.all()
    return jsonify([card.to_dict() for card in cards])

@bp.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        data = request.get_json()
        user = User(
            username=data['username'],
            email=data['email']
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User added'}), 201

    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
