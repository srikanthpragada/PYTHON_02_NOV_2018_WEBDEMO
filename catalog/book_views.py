from django.shortcuts import render, redirect
import sqlite3
from .forms import ProductForm, BookForm
from .models import Book
from django.http import JsonResponse


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
    pass


def search(request):
    return render(request, 'books/search.html')


def search_books(request):
    title = request.GET["title"]
    print("Searching for : ", title)
    # Get QuerySet of dict where each dict contains id and title
    # Method values() is used to return dict
    books = Book.objects.filter(title__contains=title).values('id', 'title')
    # Convert QuerySet to list
    books_list = list(books);
    return JsonResponse(books_list, safe=False)
