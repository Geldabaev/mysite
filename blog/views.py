from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Post
from django.utils import timezone


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts, "<<")
    return render(request, 'blog/index.html', {'posts': posts})


def categ(request, catid):
    if request.GET:
        print(request.GET)  # http://127.0.0.1:8000/cats/2/?name=Yunus&first=Geldabaev
    if int(catid) == 100:  # ручная генерация 404
        raise Http404
    if int(catid) == 50:
        return redirect('home')  # redirect 302 перемещена временно
    if int(catid) == 10:
        return redirect('home', permanent=True)  # redirect 301 перемещена на постоянно
    return HttpResponse(f"<h1>page{catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
