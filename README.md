# Lilac Lane

Lilac Lane is a modern aesthetic eCommerce website built using Django.

## Features

- Product Listing Page
- Product Detail Page
- Add to Cart System
- Increase / Decrease Quantity
- Grand Total Calculation
- User Login & Logout
- Clean Aesthetic UI

## Built With

- Python
- Django
- HTML
- CSS
- SQLite

## How to Run

python manage.py migrate  
python manage.py runserver  

Open in browser:
http://127.0.0.1:8000/

## About

Lilac Lane is a simple and elegant online shopping platform designed with a soft aesthetic theme.

## Project Structure

ecommerce/
│
├── ecommerce/                # Main project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── amezon/                   # app
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── store/
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       └── login.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── media/                    # Uploaded product images
│
├── db.sqlite3
├── manage.py
└── README.md

## To Clone It (open terminal and run)
 git clone https://github.com/umera333/ecommerce-django.git


