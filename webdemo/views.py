from django.http import HttpResponse


# Function view
def welcome(request):
    return HttpResponse("<h1>Welcome to Django!</h1>")
