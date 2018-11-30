from django.shortcuts import render, redirect
import sqlite3
from .forms import ProductForm, BookForm
from .models import Book


def home(request):
    con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
    cur = con.cursor()
    cur.execute("select count(*), avg(price) from products")
    products_count, average_price = cur.fetchone()
    con.close()
    return render(request, 'products/home.html',
                  {'products_count': products_count, 'average_price': average_price})


def list_books(request):
    return render(request, 'books/list.html', {'books': Book.objects.all()})


def add_book(request):
    if request.method == "GET":
        f = BookForm()
        return render(request, 'books/add.html', {'form': f})
    else:  # POST request
        f = BookForm(request.POST)
        if f.is_valid():
            f.save()
            f = BookForm()

        return render(request, 'books/add.html',
                      {'form': f,
                       "message": "Book has been added successfully"})


def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        message = f"Book [{id}] has been deleted!"
    except:
        message = f"Sorry! Book [{id}] not found!"

    return render(request, 'books/delete.html', {'message': message})


def edit_book(request, prodid):
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
