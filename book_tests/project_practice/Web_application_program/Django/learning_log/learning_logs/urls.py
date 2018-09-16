"""定义learning_logs的URL模式"""

from django.conf.urls import url

#导入模块 views，其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图
from . import views

#变量 urlpatterns 是一个列表，包含可在应用程序 learning_logs 中请求的网页
urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),

    #显示所有的主题
    url(r'^topics/$',views.topics,name='topics'),

    #特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]