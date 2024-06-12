from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models.user_model import Customer

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    roles = data.get("roles")

    if not username or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = Customer.find_by_username(username)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    new_customer = Customer(username, password, roles)
    new_customer.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@customer_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    customer = Customer.find_by_username(username)
    if customer and check_password_hash(customer.password_hash, password):
        # Si las credenciales son válidas, genera un token JWT
        access_token = create_access_token(
            identity={"username": username, "roles": customer.roles}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
