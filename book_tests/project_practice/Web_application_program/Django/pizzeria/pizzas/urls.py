"""定义pizzas的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    #主页
    url(r'^$',views.index, name='index'),

    #显示pizza的所有种类
    url(r'^types/$', views.types, name='types'),

    #显示每种pizza配料的页面
    url(r'^types/(?P<type_id>\d+)/$',views.toppings,name='toppings'),
]