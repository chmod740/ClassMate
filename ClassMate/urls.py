"""ClassMate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import index, register, check_register, login, check_login, liuyan, ly_detail, logout, add_liuyan, tongxun, news
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('^$', index),
    path('index.html', index),
    path('register.html', register),
    path('check_register.html', check_register),
    path('login.html', login),
    path('check_login.html', check_login),
    path('liuyan.html', liuyan),
    path('ly_detail.html', ly_detail),
    path('logout.html', logout),
    path('add_liuyan.html', add_liuyan),
    path('tongxun.html', tongxun),
    path('news.html', news),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': 'C:\\Users\\hupeng\\Desktop\\MyBlog\\static'})
]
