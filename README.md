# auto_api
REST API для продажи машин автодилерами

>### Контент
>- [Cars](https://github.com/cynimon/auto_api#cars)
>- [Dealers](https://github.com/cynimon/auto_api#dealers)
>- [Deals](https://github.com/cynimon/auto_api#deals)
>- [Обработка ошибок](https://github.com/cynimon/auto_api#обработка-ошибок)

### Запуск
- При первом запуске в PostgrSQL необходимо создать таблицу "auto_api".

- Далее в командной строке:
```shell
$ export FLASK_APP=main.py
$ flask db init
$ flask db migrate
$ flask db upgrade
$ flask run
```

### Cars

> **POST** | /cars

#### Создает новую запись в таблице Cars

- Пример запроса:

```json
{
    "brand": "Volvo",
    "amount": "5",
    "price": "26000"
}
```
- Ответ:
```json
{
  "message": "Машина марки Volvo добавлена в базу"
}
```
> **GET** | /cars

#### Считывает все записи из таблицы Cars

- Ответ:

```json
{
    "brands": [
        {
            "amount": 5,
            "brand": "Volvo",
            "price": 26000
        },
        {
            "amount": 15,
            "brand": "BMW",
            "price": 45000
        },
        {
            "amount": 3,
            "brand": "Audi",
            "price": 33000
        }
    ],
    "count": 3
}
```

> **GET** | /cars/<car_id>

#### Считывает запись из таблицы Cars с <car_id>

- Ответ:

```json
{
    "car": {
        "amount": 5,
        "brand": "Volvo",
        "price": 26000
    },
    "message": "Успешно"
}
```

> **PUT** | /cars/<car_id>
> 
#### Изменяет запись в таблице Cars с <car_id>
- Пример запроса:

```json
{
    "brand": "Volvo",
    "amount": "7",
    "price": "33000"
}
```
- Ответ:
```json
{ 
  "message": "Бренд Volvo обновлён"
}
```
---

### Dealers

> **POST** | /dealers
 
#### Создает новую запись в таблице Dealers
- Пример запроса:

```json
{
    "name": "Katten",
    "cars_sold": "0",
    "earnings": "0"
}
```
- Ответ:
```json
{
    "message": "Дилер Katten добавлен в базу"
}
```

> **GET** | /dealers
 
#### Выводит все записи из таблицы Dealers
- Ответ:
```json
{
    "count": 3,
    "dealers": [
        {
            "cars_sold": 0,
            "earnings": 0,
            "name": "Katten"
        },
        {
            "cars_sold": 256,
            "earnings": 454000,
            "name": "Sunny"
        },
        {
            "cars_sold": 10,
            "earnings": 150000,
            "name": "King"
        }
    ],
    "earned": 604000
}
```

> **GET** | /dealers/<dealer_id>

#### Считывает запись из таблицы Dealers с <dealer_id>
- Ответ:
```json
{
    "dealer": {
        "cars_sold": 0,
        "earnings": 0,
        "name": "Katten"
    },
    "message": "Успешно"
}
```

> **DELETE** | /dealers/<dealer_id>
 
#### Удаляет запись из таблицы Dealers с <dealer_id>
- Ответ:
```json
{
    "message": "Дилер Katten удалён"
}
```
---
### Deals

> **POST** | /deals

#### Создает новую запись в таблице Deals
- Пример запроса:

```json
{
	"car_id": "1",
	"dealer_id": "2",
	"amount": "3",
	"summa": "78000"
}
```
- Ответ:
```json
{
    "message": "Сделка добавлена в базу"
}
```
> **GET** | /deals
#### Выводит все записи из таблицы Deals
- Ответ:
```json
{
    "count": 3,
    "deals": [
        {
            "amount": 3,
            "car_id": 1,
            "dealer_id": 2,
            "summa": 78000
        },
        {
            "amount": 3,
            "car_id": 3,
            "dealer_id": 2,
            "summa": 99000
        },
        {
            "amount": 10,
            "car_id": 2,
            "dealer_id": 3,
            "summa": 450000
        }
    ],
    "earned": 627000
}
```
> **GET** | /deals/<deal_id>
#### Считывает запись из таблицы Deals с <deal_id>
- Ответ:
```json
{
    "deals": {
        "amount": 3,
        "car_id": 1,
        "dealer_id": 2,
        "summa": 78000
    },
    "message": "Успешно"
}
```
> **DELETE** | /deals/<deal_id>
#### Удаляет запись из таблицы Deals с <deal_id>
- Ответ:
```json
{
    "message": "Сделка удалёна"
}
```
---
### Обработка ошибок
> **400** 
- Ответ:
```json
{
    "Error": "Неверный запрос"
}
```
> **404**
- Ответ:
```json
{
    "Error": "Таких данных не существует"
}
```
> **500**
- Ответ:
```json
{
    "Error": "Ошибка сервера"
}
```
