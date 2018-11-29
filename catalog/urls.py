from django.contrib import admin
from django.urls import path
from . import views, product_views

urlpatterns = [
    path('index/', views.index),
    path('course/', views.course),
    path('products/home', product_views.home),
    path('products/list', product_views.list_products),
    path('products/add', product_views.add_product),
    path('products/add2', product_views.add_product_with_form),
    path('products/delete/<int:prodid>', product_views.delete_product),
    path('products/edit/<int:prodid>', product_views.edit_product),

]
