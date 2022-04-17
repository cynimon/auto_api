from sqlalchemy.orm import relationship
from main import db


class Deals(db.Model):
    __tablename__ = 'deals'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer(), db.ForeignKey('cars.id'))
    dealer_id = db.Column(db.Integer(), db.ForeignKey('dealers.id', ondelete='SET NULL'))
    amount = db.Column(db.Integer(), default=0)
    summa = db.Column(db.Integer(), default=0)

    cars = relationship("Cars", back_populates="deals")
    dealers = relationship("Dealers", back_populates="deals")

    def __init__(self, car_id, dealer_id, amount, summa):
        self.car_id = car_id
        self.dealer_id = dealer_id
        self.amount = amount
        self.summa = summa

    def to_json(self):
        result = {
            'car': self.cars.brand,
            'dealer': self.dealers.name,
            'amount': self.amount,
            'summa': self.summa
        }
        return result
