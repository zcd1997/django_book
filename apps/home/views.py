from django.shortcuts import render

# Create your views here.
from home.models import Category, Book


def index(request):
    categorys = Category.objects.all()
    books = Book.objects.all()[0:30]

    return render(request,'index.html',{'categorys':categorys,'books':books})