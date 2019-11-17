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
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', include('qa.urls'), name='root'),
    re_path(r'^login/', include('qa.urls'), name='login'),
    re_path(r'^signup/', include('qa.urls'), name='signup'),
    re_path(r'^question/\d+/', include('qa.urls'), name='question'),
    re_path(r'^ask/', include('qa.urls'), name='ask'),
    re_path(r'^popular/', include('qa.urls'), name='popular'),
    re_path(r'^new/', include('qa.urls'), name='new'),
    # url(r'^\S*/', include('qa.urls'), name='other'),

]
