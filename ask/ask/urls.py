"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import re_path
# from django.contrib import admin

urlpatterns = [
    re_path(r'(?P<name>^$)', 'qa.views.test', name='root'),
    re_path(r'(?P<name>^login)/', 'qa.views.test', name='login'),
    re_path(r'(?P<name>^signup)/', 'qa.views.test', name='signup'),
    re_path(r'(?P<name>^question/\d+)/', 'qa.views.test', name='question'),
    re_path(r'(?P<name>^ask)/', 'qa.views.test', name='ask'),
    re_path(r'(?P<name>^popular)/', 'qa.views.test', name='popular'),
    re_path(r'(?P<name>^new)/', 'qa.views.test', name='new'),
    re_path(r'(?P<name>^\w+)/', 'qa.views.test', name='other'),

]
