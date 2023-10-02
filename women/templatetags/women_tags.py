from django import template
from women.models import *

register = template.Library()

def get_categories():
    return Category.objects.all()

@register.simple_tag(name='getcats')      #простой пользовательский тег для использования его в шаблонах
def get_categories(filter=None):
    #if not filter:
        return Category.objects.all()
    #else:
       # return Category.objects.all(pk=filter)
    

@register.inclusion_tag('list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
 
    return {"cats": cats, "cat_selected": cat_selected}
