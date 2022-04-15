from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Dealers(db.Model):
    __tablename__ = 'dealers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    cars_sold = db.Column(db.Integer(), default=0)
    earnings = db.Column(db.Integer(), default=0)

    deals = relationship("Deals", back_populates="dealers")

    def __init__(self, name, cars_sold, earnings):
        self.name = name
        self.cars_sold = cars_sold
        self.earnings = earnings

    def __repr__(self):
        return f'<Dealer {self.name}'
