from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

def index(request):
   posts = Women.objects.all()
   cats = Category.objects.all()
   context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
   } 
   return render(request, 'index.html', context=context)

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

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    cats = Category.objects.all() 
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    } 
    return render(request, 'index.html', context=context)
