"""djan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.urls import re_path

from rgc.models.person import Person

info_dict = {
	'queryset': Person.objects.all(),
	'date_field': 'time',
}
from rgc.views import index, reg, new_reg, new_reg1, register, export, post, redis, cookie_random, \
	cache_pub, cache_pri

app_name = 'rgc'
urlpatterns = [
	path('index/', index),
	re_path('^reg/$', reg),
	path('new_reg/<int:a>/<int:b>/', new_reg),
	path('new_reg1/', new_reg1),
	path('register/', register),
	path('export/', export),
	path('post/', post),
	path('redis/', redis),  # redis缓存测试
	path('cookie_random/', cookie_random),  # redis缓存测试
	path('cache_pub/', cache_pub),  # redis缓存测试
	path('cache_pri/', cache_pri),  # redis缓存测试
	path('sitemap.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
		 name='django.contrib.sitemaps.views.sitemap'),
]
