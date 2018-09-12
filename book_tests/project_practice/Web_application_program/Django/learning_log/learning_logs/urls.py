"""定义learning_logs的URL模式"""

from django.conf.urls import url

#导入模块 views，其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图
from . import views

#变量 urlpatterns 是一个列表，包含可在应用程序 learning_logs 中请求的网页
urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),
]