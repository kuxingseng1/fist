# 实现留言板views视图层
from django.http import HttpResponse
from django.shortcuts import render
from .import models


def message_form(request):
    return render(request, 'fist.html')


def message(request):

    # print(request.read)
    if request.GET["name"] and request.GET["title"]:
        book = models.Book(name=request.GET["name"],title=request.GET["title"])
        book.save()
        return render(request, 'message.html')
    else:
        print("error")

def find_book(request):
    lists=[]
    books=models.Book.objects.filter(name=request.GET["name"])
    print("[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
    for i in books:
        lists.append(i.title)
    print(lists)
    return render(request,"search-form.html", {"messagelist": lists})
