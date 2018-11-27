from django.shortcuts import render
import sqlite3
from .models import Course
from django.http import HttpResponse


def home(request):
    return render(request, 'products/home.html')


def list_products(request):
    con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
    cur = con.cursor()
    cur.execute("select * from products")
    products = cur.fetchall()
    # print(products)
    con.close()
    return render(request, 'products/list.html',
                   {'products' : products})


def add_product(request):
    return render(request, 'products/add.html')