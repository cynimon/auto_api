from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Cars import Cars
from Dealers import Dealers
from Deals import Deals

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sasha:11qa@localhost:5432/auto_api"
# установка сессии
db = SQLAlchemy(app)
migrate = Migrate(app, db)

'''выполнение сделок - добавление и удаление, 
изменения в связанных таблицах'''


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


'''endpoint /cars'''


@app.route('/cars', methods=['POST', 'GET'])
def with_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = Cars(brand=data['brand'], amount=data['amount'], price=data['price'])
            db.session.add(new_car)
            db.session.commit()
            return {'message': f'Машина марки {new_car.brand} добавлена в базу'}
        else:
            return {'error': 'Данные предоставлены не в формате JSON'}
    elif request.method == 'GET':
        cars = Cars.query.all()
        results = [
            {
                "brand": car.brand,
                "amount": car.amount,
                "price": car.price
            } for car in cars]

        return {"count": len(results), "brands": results}


'''endpoint /cars/<car_id>'''


@app.route('/cars/<car_id>', methods=['GET', 'PUT'])
def with_car(car_id):
    car = Cars.query.get_or_404(car_id)

    if request.method == 'GET':
        response = {
            "brand": car.brand,
            "amount": car.amount,
            "price": car.price
        }
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


@app.route('/dealers', methods=['POST', 'GET'])
def with_dealers():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_dealer = Dealers(name=data['name'], cars_sold=data['cars_sold'], earnings=data['earnings'])
            db.session.add(new_dealer)
            db.session.commit()
            return {"message": f"Дилер {new_dealer.name} добавлен в базу"}
        else:
            return {"error": "Данные предоставлены не в формате JSON"}
    elif request.method == 'GET':
        dealers = Dealers.query.all()
        results = [
            {
                "name": dealer.name,
                "cars_sold": dealer.cars_sold,
                "earnings": dealer.earnings
            } for dealer in dealers]
        earned = sum([int(dealer.earnings) for dealer in dealers])

        return {"count": len(results), "dealers": results, "earned": earned}


'''endpoint /dealers/<dealer_id>'''


@app.route('/dealers/<dealer_id>', methods=['GET', 'DELETE'])
def with_dealer(dealer_id):
    dealer = Dealers.query.get_or_404(dealer_id)

    if request.method == 'GET':
        response = {
            "name": dealer.name,
            "cars_sold": dealer.cars_sold,
            "earnings": dealer.earnings
        }
        return {"message": "Успешно", "dealer": response}
    elif request.method == 'DELETE':
        db.session.delete(dealer)
        db.session.commit()
        return {"message": f"Дилер {dealer.name} удалён"}


'''endpoint /deals'''


@app.route('/deals', methods=['POST', 'GET'])
def with_deals():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_deal = Deals(car_id=data['car_id'], dealer_id=data['dealer_id'], amount=data['amount'],
                             summa=data['summa'])
            db.session.add(new_deal)
            update_dealers_cars(request.method, data)
            db.session.commit()
            return {"message": "Сделка добавлена в базу"}
        else:
            return {"error": "Данные предоставлены не в формате JSON"}
    elif request.method == 'GET':
        deals = Deals.query.all()
        results = [{
            "car_id": deal.car_id,
            "dealer_id": deal.dealer_id,
            "amount": deal.amount,
            "summa": deal.summa
        } for deal in deals]
        earned = sum([int(deal.summa) for deal in deals])
        return {"count": len(results), "deals": results, "earned": earned}


'''endpoin /deals/<deal_id>'''


@app.route('/deals/<deal_id>', methods=['GET', 'DELETE'])
def with_deal(deal_id):
    deal = Deals.query.get_or_404(deal_id)
    response = {
        "car_id": deal.car_id,
        "dealer_id": deal.dealer_id,
        "amount": deal.amount,
        "summa": deal.summa
    }
    if request.method == 'GET':
        return {"message": "Успешно", "deals": response}
    elif request.method == 'DELETE':
        update_dealers_cars(request.method, response)
        db.session.delete(deal)
        db.session.commit()
        return {"message": f"Сделка удалёна"}


if __name__ == '__main__':
    app.run(debug=True)
