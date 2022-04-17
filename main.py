from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import werkzeug.exceptions


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sasha:11qa@localhost:5432/auto_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# установка сессии
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# импорт после создания db, чтобы избежать ошибки импорта
from Cars import Cars
from Dealers import Dealers
from Deals import Deals
import handle_data as hd

"""Обработчик кодов ошибок HTTP"""


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return {"Error": "Неверный запрос"}, 400


@app.errorhandler(werkzeug.exceptions.NotFound)
def hande_not_found(e):
    return {"Error": "Таких данных не существует"}, 404


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def hande_not_found(e):
    return {"Error": "Ошибка сервера"}, 500


'''endpoint /cars'''

"""Новая запись в Cars на POST, вывод всех записей Cars на GET"""


@app.route('/cars', methods=['POST', 'GET'])
def with_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = Cars(brand=data['brand'], amount=data['amount'], price=data['price'])
            db.session.add(new_car)
            db.session.commit()
            return {'message': f'Машина марки {new_car.brand} добавлена в базу'}
    elif request.method == 'GET':
        response = hd.get_all_rows(Cars)
        return {"count": len(response), "brands": response}


'''endpoint /cars/<car_id>'''

"""Вывод записи по id на GET, редактирование на PUT"""


@app.route('/cars/<car_id>', methods=['GET', 'PUT'])
def with_car(car_id):
    car, response = hd.get_dict_response(Cars, car_id)
    if request.method == 'GET':
        return {"message": "Успешно", "car": response}
    elif request.method == 'PUT':
        data = request.get_json()
        car.brand = data['brand']
        car.amount = data['amount']
        car.price = data['price']
        db.session.add(car)
        db.session.commit()
        return {"message": f"Бренд {car.brand} обновлён"}


'''endpoint /dealers'''

"""Новая запись в Dealers на POST, вывод всех записей Dealers на GET"""


@app.route('/dealers', methods=['POST', 'GET'])
def with_dealers():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_dealer = Dealers(name=data['name'], cars_sold=data['cars_sold'], earnings=data['earnings'])
            db.session.add(new_dealer)
            db.session.commit()
            return {"message": f"Дилер {new_dealer.name} добавлен в базу"}
    elif request.method == 'GET':
        response = hd.get_all_rows(Dealers)
        earned = sum([int(dealer['earnings']) for dealer in response])
        return {"count": len(response), "dealers": response, "earned": earned}


'''endpoint /dealers/<dealer_id>'''

"""Вывод записи по id на GET, удаление на DELETE"""


@app.route('/dealers/<dealer_id>', methods=['GET', 'DELETE'])
def with_dealer(dealer_id):
    dealer, response = hd.get_dict_response(Dealers, dealer_id)
    if request.method == 'GET':
        return {"message": "Успешно", "dealer": response}
    elif request.method == 'DELETE':
        db.session.delete(dealer)
        db.session.commit()
        return {"message": f"Дилер {dealer.name} удалён"}


'''endpoint /deals'''

"""Новая запись в Deals на POST, вывод всех записей Deals на GET"""


@app.route('/deals', methods=['POST', 'GET'])
def with_deals():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_deal = Deals(car_id=data['car_id'], dealer_id=data['dealer_id'], amount=data['amount'],
                             summa=data['summa'])
            db.session.add(new_deal)
            hd.update_dealers_cars(request.method, data)
            db.session.commit()
            return {"message": "Сделка добавлена в базу"}
    elif request.method == 'GET':
        response = hd.get_all_rows(Deals)
        earned = sum([int(deal['summa']) for deal in response])
        return {"count": len(response), "deals": response, "earned": earned}


'''endpoin /deals/<deal_id>'''

"""Вывод записи по id на GET, удаление на DELETE"""


@app.route('/deals/<deal_id>', methods=['GET', 'DELETE'])
def with_deal(deal_id):
    deal, response = hd.get_dict_response(Deals, deal_id)
    if request.method == 'GET':
        return {"message": "Успешно", "deals": response}
    elif request.method == 'DELETE':
        hd.update_dealers_cars(request.method, response)
        db.session.delete(deal)
        db.session.commit()
        return {"message": f"Сделка удалёна"}


if __name__ == '__main__':
    app.run(debug=True)
