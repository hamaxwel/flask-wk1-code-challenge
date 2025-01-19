from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import app, db
from models import User, Item

def register_routes(app):
    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201

    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"message": "Invalid credentials"}), 401

    @app.route("/current_user", methods=["GET"])
    @jwt_required()
    def current_user():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        return jsonify(username=user.username, email=user.email), 200

    @app.route("/logout", methods=["POST"])
    @jwt_required()
    def logout():
        return jsonify({"message": "Logout successful"}), 200

    @app.route("/user/update", methods=["PUT"])
    @jwt_required()
    def update_user():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200

    @app.route("/user/updatepassword", methods=["PUT"])
    @jwt_required()
    def update_password():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        data = request.get_json()
        user.set_password(data['password'])
        db.session.commit()
        return jsonify({"message": "Password updated successfully"}), 200

    @app.route("/user/delete_account", methods=["DELETE"])
    @jwt_required()
    def delete_account():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Account deleted successfully"}), 200

    @app.route("/items", methods=["POST"])
    @jwt_required()
    def create_item():
        data = request.get_json()
        new_item = Item(name=data['name'], description=data['description'], price=data['price'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item created successfully"}), 201

    @app.route("/items", methods=["GET"])
    def get_items():
        items = Item.query.all()
        return jsonify([{"id": item.id, "name": item.name, "description": item.description, "price": item.price} for item in items]), 200

    @app.route("/items/<int:item_id>", methods=["PUT"])
    @jwt_required()
    def update_item(item_id):
        item = Item.query.get(item_id)
        data = request.get_json()
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.price = data.get('price', item.price)
        db.session.commit()
        return jsonify({"message": "Item updated successfully"}), 200

    @app.route("/items/<int:item_id>", methods=["DELETE"])
    @jwt_required()
    def delete_item(item_id):
        item = Item.query.get(item_id)
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item deleted successfully"}), 200