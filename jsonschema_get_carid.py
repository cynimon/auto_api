{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Car_id GET",
    "description": "Вывод записей для машины с указанным car_id",
    "type": "object",

    "properties": {

        "car": {
            "description": "Название марки машины",
            "type": "string"
        },

        "amount": {
            "type": "integer",
            "minimum": 0,
        },

        "price": {
            "type": "integer",
            "minimum": 0,
        },
        "message": {
            "description": "Успешное выполнение (код 200)",
            "type": "string"
        }
    }
}
