import json

from flask_login import CustomerMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import db


class Customer(CustomerMixin, db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    passwordd = db.Column(db.String(128), nullable=False)
    phone= db.Column(db.String(50),  nullable=False)
    roles = db.Column(db.String(50), nullable=False)

    def __init__(self, name, password,email,phone, roles=["Customer"]):
        
        self.name = name
        self.email = email
        self.phone = phone
        self.roles = json.dumps(roles)
        self.passwordd = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    # Esta funcion encuentra un usuario por su nombre de usuario
    @staticmethod
    def find_by_Customername(name):
        return Customer.query.filter_by(name=name).first()