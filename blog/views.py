from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, "blog/index.html", {})


def categ(request, catid):
    return HttpResponse(f"<h1>page{catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
