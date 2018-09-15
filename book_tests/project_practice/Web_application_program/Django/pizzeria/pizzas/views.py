from django.shortcuts import render

from .models import Pizza
from .models import Topping
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'pizzas/index.html')

def types(request):
    """显示所有的pizza种类"""
    types = Pizza.objects.all()
    context = {'types':types}
    return render(request,'pizzas/types.html',context)

def toppings(request,type_id):
    """显示每种pizza的配料"""
    type = Pizza.objects.get(id=type_id)
    toppings = type.topping_set.all()
    context = {'type':type, 'toppings':toppings}
    return render(request, 'pizzas/toppings.html',context)