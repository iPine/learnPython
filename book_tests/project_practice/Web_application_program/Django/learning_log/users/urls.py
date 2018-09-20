"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

LoginView.template_name = 'users/login.html'
urlpatterns = [
    #登录页面
    path('login/',LoginView.as_view(), name='login'),
]