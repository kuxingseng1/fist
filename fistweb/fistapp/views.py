from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def hello(request):
    # hell = "hell"
    return HttpResponse("{hell: hell}")


def fistappmodel(request):
    # hell = "hell"
    return HttpResponse("我是fistapp的地址")


def find_book(request):
    books=models.Book.objects.all()
    for i in books:
        list.append(i.title)
    return HttpResponse(list)