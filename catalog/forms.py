import django.forms as forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=30, label="Product Name")
    price = forms.IntegerField(min_value=1, label="Product Price")
    qoh = forms.IntegerField(min_value=0, label="Quantity On Hand")
