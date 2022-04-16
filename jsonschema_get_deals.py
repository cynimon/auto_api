{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Deals GET",
    "description": "Вывод всех записей из таблицы Deals",
    "type": "object",
    "properties": {

        "count": {
            "description": "Подсчет количества записей",
            "type": "integer"
        },

        "earned": {
            "description": "Подсчет суммы всех сделок в таблице",
            "type": "integer"
        },

        "brands": {
            "description": "Записи из таблицы",
            "type": "array",
            "items": {
                "type": "dict"
            }
        }

    }
}
