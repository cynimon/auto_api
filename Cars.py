from sqlalchemy.orm import relationship
from main import db


class Cars(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(), unique=True)
    amount = db.Column(db.Integer(), default=0)
    price = db.Column(db.Integer(), default=0)

    deals = relationship("Deals", back_populates="cars")

    def __init__(self, brand, amount, price):
        self.brand = brand
        self.amount = amount
        self.price = price

    def __repr__(self):
        return f'Car {self.brand}'

    def to_json(self):
        result = {
            'brand': self.brand,
            'amount': self.amount,
            'price': self.price
        }
        return result
