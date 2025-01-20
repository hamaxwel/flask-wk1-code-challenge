from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from models import Item

item_bp = Blueprint('item', __name__)

@item_bp.route("/items", methods=["POST"])
@jwt_required()
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'], price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item created successfully"}), 201

@item_bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "description": item.description, "price": item.price} for item in items]), 200

@item_bp.route("/items/<int:item_id>", methods=["PUT"])
@jwt_required()
def update_item(item_id):
    item = Item.query.get(item_id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    db.session.commit()
    return jsonify({"message": "Item updated successfully"}), 200

@item_bp.route("/items/<int:item_id>", methods=["DELETE"])
@jwt_required()
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"}), 200