{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Car",
    "description": "Параметры для записей в таблицу Car",
    "type": "object",

    "properties": {

        "brand": {
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
        }
    },

    "required": ["brand", "amount", "price"]
}
