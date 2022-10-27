# Task to create and view customer orders

## Requirements
- Python 3.8
- Django 4.1
- Django REST Framework

## Installation
Create a virtual environment in your project directory
```
python3 -m venv venv
```

Activate the virtual environment
```
source venv/bin/activate
```

Install all the required dependencies by running
```
pip install -r requirements.txt
```
## Django migration

Create the database tables
```
python manage.py migrate
```
Create the superuser
```
python manage.py createsuperuser
```

## To execute

Run the Django server by running
```
python manage.py runserver
```

We can test the API using [curl] or we can use [Postman](https://www.postman.com/)
### Login to get the JWT token
```
curl --location --request POST 'http://127.0.0.1:8000/api/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test",
    "password":"test"
}'
```
### Product Create
```
curl --location --request POST 'http://127.0.0.1:8000/api/products/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUwMjU1LCJpYXQiOjE2NjY4NDk5NTUsImp0aSI6IjJhYmU1Nzk2NzM3NjQyYTM4YTQ5MjA0NWMzNjExZmVhIiwidXNlcl9pZCI6MX0.lPXLmxOK68ZRNnB8YMDtKItmVe0E8NVOqAYeEaQ4TOc' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Apple iPhone 12",
    "stock_qty":"1000",
    "price":"100.99"
}'
```

### Product List
```
curl --location --request GET 'http://127.0.0.1:8000/api/products' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUwMjU1LCJpYXQiOjE2NjY4NDk5NTUsImp0aSI6IjJhYmU1Nzk2NzM3NjQyYTM4YTQ5MjA0NWMzNjExZmVhIiwidXNlcl9pZCI6MX0.lPXLmxOK68ZRNnB8YMDtKItmVe0E8NVOqAYeEaQ4TOc' \
--data-raw ''
```

The result:
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Apple iPhone 10",
            "price": "59.99",
            "stock_qty": 500
        },
        {
            "id": 2,
            "name": "Apple iPhone 12",
            "price": "100.99",
            "stock_qty": 1000
        }
    ]
}
```
### Product View
```
curl --location --request GET 'http://127.0.0.1:8000/api/products/2' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUwMjU1LCJpYXQiOjE2NjY4NDk5NTUsImp0aSI6IjJhYmU1Nzk2NzM3NjQyYTM4YTQ5MjA0NWMzNjExZmVhIiwidXNlcl9pZCI6MX0.lPXLmxOK68ZRNnB8YMDtKItmVe0E8NVOqAYeEaQ4TOc' \
--data-raw ''
```

The result:
```
{
    "id": 2,
    "name": "Apple iPhone 12",
    "price": "100.99",
    "stock_qty": 1000
}
```
### Customer Create
```
curl --location --request POST 'http://127.0.0.1:8000/api/customers/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUwMjU1LCJpYXQiOjE2NjY4NDk5NTUsImp0aSI6IjJhYmU1Nzk2NzM3NjQyYTM4YTQ5MjA0NWMzNjExZmVhIiwidXNlcl9pZCI6MX0.lPXLmxOK68ZRNnB8YMDtKItmVe0E8NVOqAYeEaQ4TOc' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name":"John",
    "last_name":"Doe",
    "email":"John.doe@test.com"
}'
```
### Customer List
```
curl --location --request GET 'http://127.0.0.1:8000/api/customers' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUwMjU1LCJpYXQiOjE2NjY4NDk5NTUsImp0aSI6IjJhYmU1Nzk2NzM3NjQyYTM4YTQ5MjA0NWMzNjExZmVhIiwidXNlcl9pZCI6MX0.lPXLmxOK68ZRNnB8YMDtKItmVe0E8NVOqAYeEaQ4TOc' \
--data-raw ''
```
The result:
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@test.com"
        }
    ]
}
```
### Order Create
```
curl --location --request POST 'http://127.0.0.1:8000/api/orders/order/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUwMjU1LCJpYXQiOjE2NjY4NDk5NTUsImp0aSI6IjJhYmU1Nzk2NzM3NjQyYTM4YTQ5MjA0NWMzNjExZmVhIiwidXNlcl9pZCI6MX0.lPXLmxOK68ZRNnB8YMDtKItmVe0E8NVOqAYeEaQ4TOc' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer":"1"
}'
```
### Order List - Filter by customer to see orders per customer
```
curl --location --request GET 'http://127.0.0.1:8000/api/orders/order?customer=1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUyMDk5LCJpYXQiOjE2NjY4NTE3OTksImp0aSI6IjRjZDU5MDFlN2U1YjRiMmFiMDM2ZTFjNWIyY2Y5MjBkIiwidXNlcl9pZCI6MX0.nIgUzVGthkRzPVUWI0VRWJMAuXSnC5GGpgbdLMy7lpw' \
--data-raw ''
```
The result:
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "order_date": "2022-10-27T06:57:44.212096Z",
            "customer": 1,
            "items": [
                {
                    "id": 1,
                    "order": 1,
                    "product": {
                        "id": 2,
                        "name": "Apple iPhone 7",
                        "price": "50.99",
                        "stock_qty": 180
                    },
                    "qty": 20
                },
                {
                    "id": 2,
                    "order": 1,
                    "product": {
                        "id": 1,
                        "name": "Apple iPhone 12",
                        "price": "100.99",
                        "stock_qty": 985
                    },
                    "qty": 15
                }
            ]
        }
    ]
}
```
### Order Item Create
```
curl --location --request POST 'http://127.0.0.1:8000/api/orders/items/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2ODUyMDk5LCJpYXQiOjE2NjY4NTE3OTksImp0aSI6IjRjZDU5MDFlN2U1YjRiMmFiMDM2ZTFjNWIyY2Y5MjBkIiwidXNlcl9pZCI6MX0.nIgUzVGthkRzPVUWI0VRWJMAuXSnC5GGpgbdLMy7lpw' \
--header 'Content-Type: application/json' \
--data-raw '{
    "order":"1",
    "product":"2",
    "qty":"20"
}'
```
## To test

Run the Django tests by running
```
python manage.py test
```
## To still be completed
```
- Adjust the stock quantity on update and delete of an order
- Add fulfilled flag for orders
- Implement tests
- Adjust order create /update to cater for adding/updating many order items at once.
- add ordering to list results
- Could use Swagger for documentation
```
