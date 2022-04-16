{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Cars GET",
    "description": "Вывод всех записей из таблицы Cars",
    "type": "object",
    "properties": {

        "count": {
            "description": "Подсчет количества записей",
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
