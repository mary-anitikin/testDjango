from django.urls import path, re_path
 
from .views import *
 
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
#    path('cats/', categoriesone, name='cats'),
#    path('cats/<slug:cat>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]

