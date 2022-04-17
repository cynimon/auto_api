from main import db
from Cars import Cars
from Dealers import Dealers

"""Выполнение сделок - изменения в связанных с Deals таблицах"""


def update_dealers_cars(method, data):
    dealer = Dealers.query.get(int(data['dealer_id']))
    car = Cars.query.get(int(data['car_id']))

    if method == 'POST':
        dealer.cars_sold += int(data['amount'])
        dealer.earnings += int(data['summa'])
        car.amount -= int(data['amount'])
    elif method == 'DELETE':
        dealer.cars_sold -= int(data['amount'])
        dealer.earnings -= int(data['summa'])
        car.amount += int(data['amount'])

    db.session.add(dealer)
    db.session.add(car)
    db.session.commit()
    return


"""Получение модели из базы по id"""


def get_dict_response(model, model_id):
    anymodel = model.query.get_or_404(model_id)
    return anymodel, anymodel.to_json()


"""Получение всех записей модели"""


def get_all_rows(model):
    allmod = model.query.all()
    templi = [onemod.to_json() for onemod in allmod]
    return templi
