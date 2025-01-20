from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import User

user_bp = Blueprint('user', __name__)

@user_bp.route("/user/update", methods=["PUT"])
@jwt_required()
def update_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200

@user_bp.route("/user/updatepassword", methods=["PUT"])
@jwt_required()
def update_password():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    data = request.get_json()
    user.set_password(data['password'])
    db.session.commit()
    return jsonify({"message": "Password updated successfully"}), 200

@user_bp.route("/user/delete_account", methods=["DELETE"])
@jwt_required()
def delete_account():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Account deleted successfully"}), 200

@user_bp.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users]), 200