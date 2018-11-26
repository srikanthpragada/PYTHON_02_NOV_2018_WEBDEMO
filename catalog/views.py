from django.shortcuts import render
from .models import Course
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def course(request):
    c = Course("Django Framework", 'Srikanth',
               ['Templates', 'Forms', 'State Management', 'ORM', 'AJAX', 'REST API'])
    # render(requests,template,context)
    return render(request, 'course-info.html', {'course': c})
