import django.forms as forms
from .models import Book


class ProductForm(forms.Form):
    name = forms.CharField(max_length=30, label="Product Name")
    price = forms.IntegerField(min_value=1, label="Product Price")
    qoh = forms.IntegerField(min_value=0, label="Quantity On Hand")


# Create form from Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
