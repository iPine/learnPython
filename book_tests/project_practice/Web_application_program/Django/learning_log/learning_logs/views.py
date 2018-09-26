from django.shortcuts import render, get_object_or_404
#新网页new_topic的视图函数需要的包
from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm,EntryForm



# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    """显示所有的主题"""
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目"""
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    # 确认请求的主题属于当前用户
    # if topic.owner != request.user:
    #     raise Http404
    check_topic_owner(request,topic.owner)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据，则创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            # form.save()
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(request,topic.owner)

    if request.method != 'POST':
        #未提交数据，则创建一个新表单
        form = EntryForm()
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            #不保存到数据库
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            #获取topic页面的URL，并传给HttpResponseRedirect，再重定向到特定的id为topic_id的topic页面
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

    context = {'topic':topic, 'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    # entry = Entry.objects.get(id=entry_id)
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    # if topic.owner != request.user:
    #     raise Http404
    check_topic_owner(request,topic.owner)

    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

    context = {'entry': entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)


# 验证所请求的数据是否属于当前登录的用户
def check_topic_owner(request,owner):
        if owner != request.user:
            raise Http404