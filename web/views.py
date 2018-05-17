from django.shortcuts import render, render_to_response
from web.tool import get_location
from web.models import Access_log, News, User, LiuYan
from django.shortcuts import HttpResponse, HttpResponseRedirect
import json

# Create your views here.
def index(req):
    at = req.COOKIES.get('AccessTime', None)
    if True:
        access_log = Access_log()
        access_log.ip_address = req.META.get('REMOTE_ADDR')
        access_log.user_agent = req.META.get('HTTP_USER_AGENT')
        access_log.location = get_location(access_log.ip_address)
        access_log.save()
    at = Access_log.objects.all().count()
    news = News.objects.all()
    username = req.session.get('username', None)
    name = req.session.get('name', None)
    response = render_to_response('index.html',
                                  {'access_time': at,
                                   'news': news,
                                   'username': username,
                                   'name': name})
    response.set_cookie(key='AccessTime', value=at, max_age=None)
    return response

def register(req):
    username = req.session.get('username', None)
    name = req.session.get('name', None)
    at = Access_log.objects.all().count()
    response = render_to_response('register.html',
                                  {'access_time': at,
                                   'username': username,
                                   'name': name})
    response.set_cookie(key='AccessTime', value=at, max_age=None)
    return response

def check_register(req):
    username = req.GET['username']
    name = req.GET['name']
    password = req.GET['password']
    if len(User.objects.filter(username__exact=username)) == 0:
        user = User()
        user.username = username
        user.password = password
        user.name = name
        user.save()
        result = {'rst': 0, 'msg': '注册成功'}
    else:
        result = {'rst': -1, 'msg': '用户已经存在'}
    return HttpResponse(json.dumps(result), content_type='application/json')

def login(req):
    username = req.session.get('username', None)
    name = req.session.get('name', None)
    at = Access_log.objects.all().count()
    response = render_to_response('login.html',
                                  {'access_time': at,
                                   'username': username,
                                   'name': name})
    response.set_cookie(key='AccessTime', value=at, max_age=None)
    return response

def check_login(req):
    username = req.GET['username']
    password = req.GET['password']
    users = User.objects.filter(username__exact=username, password__exact=password)
    if(len(users)>0):
        req.session['username'] = username
        req.session['name'] = users[0].name
        result = {'rst': 0, 'msg': '登录成功'}
    else:
        result = {'rst': -1, 'msg': '登录失败，用户名或者密码错误'}
    return HttpResponse(json.dumps(result), content_type='application/json')

def liuyan(req):
    username = req.session.get('username', None)
    name = req.session.get('name', None)
    jump = None
    if req.session.get('username') is None:
        jump = 'alert("请先登录！");window.location.href="login.html" '
    at = Access_log.objects.all().count()
    response = render_to_response('liuyan.html',
                                  {'access_time': at, 'jump': jump,
                                   'username': username,
                                   'name': name})
    response.set_cookie(key='AccessTime', value=at, max_age=None)
    return response

def ly_detail(req):
    username = req.session.get('username', None)
    name = req.session.get('name', None)
    lys = LiuYan.objects.all()
    return render_to_response('liuyan_detail.html', {'lys': lys})


def logout(req):
    req.session.clear()
    return HttpResponseRedirect('index.html')
def add_liuyan(req):
    content = req.GET['content']
    username = req.session['username']
    name = req.session.get('name', None)
    ly = LiuYan()
    ly.username = username
    ly.content = content
    ly.save()
    result = {'rst': 0, 'msg': '留言成功'}
    return HttpResponse(json.dumps(result), content_type='application/json')

def tongxun(req):
    username = req.session.get('username', None)
    name = req.session.get('name', None)
    at = Access_log.objects.all().count()
    response = render_to_response('tongxun.html',
                                  {'access_time': at,
                                   'username': username,
                                   'name': name})
    response.set_cookie(key='AccessTime', value=at, max_age=None)
    return response

def news(req):
    id = req.GET['id']
    new = News.objects.filter(id__exact = id)[0]
    username = req.session.get('username', None)
    name = req.session.get('name', None)
    at = Access_log.objects.all().count()
    response = render_to_response('news.html',
                                  {'access_time': at,
                                   'username': username,
                                   'new': new,
                                   'name': name})
    response.set_cookie(key='AccessTime', value=at, max_age=None)
    return response