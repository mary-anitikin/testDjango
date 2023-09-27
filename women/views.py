from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
   posts = Women.objects.all()
   return render(request, 'index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def categories(request, cat):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")

def categoriesone(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

def archive(request, year):
    # if(int(year) > 2020):
    raise Http404()    
    # return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница, к сожалению, не найдена</h1>')

def about(request):
    return render(request, 'about.html', {'menu': menu, 'title': 'О сайте'})