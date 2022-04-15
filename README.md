# auto_api
REST API для продажи машин автодилерами

###Cars

>> **POST** | /cars
>
> Создает новую запись в таблице Cars

'''json
{
	"brand": "Volvo",
	"amount": "5",
	"price": "26000"
}
'''

> >**GET** | /cars
> 
> Считывает все записи из таблицы Cars

> >**GET** | /cars/<car_id>
> 
> Считывает запись из таблицы Cars с <car_id>

> >**PUT** | /cars/<car_id>
> 
> Изменяет запись в таблице Cars с <car_id>

###Dealers

> >**POST** | /dealers
> 
> Создает новую запись в таблице Dealers


> >**GET** | /dealers
> 
> Выводит все записи из таблицы Dealers


> >**GET** | /dealers/<dealer_id>
> 
> Считывает запись из таблицы Dealers с <dealer_id>


> >**DELETE** | /dealers/<dealer_id>
> 
> Удаляет запись из таблицы Dealers с <dealer_id>

###Deals

>> **POST** | /deals
> 
> Создает новую запись в таблице Deals


>> **GET** | /deals
> 
> Выводит все записи из таблицы Deals


>> **GET** | /deals/<deal_id>
> 
> Считывает запись из таблицы Deals с <deal_id>


> >**DELETE** | /deals/<deal_id>
> 
> Удаляет запись из таблицы Deals с <deal_id>
