from django.shortcuts import render, redirect
import sqlite3
from .models import Course
from django.http import HttpResponse


def home(request):
    con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
    cur = con.cursor()
    cur.execute("select count(*), avg(price) from products")
    products_count, average_price = cur.fetchone()
    con.close()
    return render(request, 'products/home.html',
                  {'products_count': products_count, 'average_price': average_price})


def list_products(request):
    con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
    cur = con.cursor()
    cur.execute("select * from products")
    products = cur.fetchall()
    # print(products)
    con.close()
    return render(request, 'products/list.html',
                  {'products': products})


def add_product(request):
    if request.method == "GET":
        return render(request, 'products/add.html')
    else:  # POST request
        name = request.POST["prodname"]
        price = request.POST["price"]
        qoh = request.POST["qoh"]
        con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
        cur = con.cursor()
        cur.execute("insert into products(prodname,price,qoh) values(?,?,?)",
                    (name, price, qoh))
        con.commit()
        con.close()
        return render(request, 'products/add.html',
                      {"message": "Product has been added successfully"})


def delete_product(request, prodid):
    con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
    cur = con.cursor()
    cur.execute("delete from products where prodid = ?", (prodid,))
    if cur.rowcount == 1:
        con.commit()
        message = f"Product [{prodid}] has been deleted successfully!"
    else:
        message = f"Product [{prodid}] was not found!"
    con.close()
    return render(request, 'products/delete.html', {'message': message})


def edit_product(request, prodid):
    con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
    cur = con.cursor()
    if request.method == "GET":
        cur.execute("select * from products where prodid = ?", (prodid,))
        product = cur.fetchone()
        con.close()
        return render(request, 'products/edit.html', {'product': product})
    else:  # POST request
        name = request.POST["prodname"]
        price = request.POST["price"]
        qoh = request.POST["qoh"]
        con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
        cur = con.cursor()
        cur.execute("update products set prodname = ?, price = ?, qoh = ? where prodid = ?",
                    (name, price, qoh, prodid))
        con.commit()
        con.close()
        return redirect("/catalog/products/list")
