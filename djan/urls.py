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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.urls import re_path

from rgc.models import Person
from rgc.views import index, reg, new_reg, new_reg1, register, debug_view, export, post, redis, cookie_random, \
	cache_pub, cache_pri

info_dict = {
	'queryset': Person.objects.all(),
	'date_field': 'time',
}
urlpatterns = [
	path('admin/', admin.site.urls),
	path('index/', index),
	re_path('^reg/$', reg),
	path('new_reg/<int:a>/<int:b>/', new_reg),
	path('new_reg1/', new_reg1),
	path('register/', register),
	path('export/', export),
	path('post/', post),
	path('accounts/', include(auth_urls)),  # 用户注册系统
	path('redis/', redis),  # redis缓存测试
	path('cookie_random/', cookie_random),  # redis缓存测试
	path('cache_pub/', cache_pub),  # redis缓存测试
	path('cache_pri/', cache_pri),  # redis缓存测试
	path('sitemap.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
		 name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
	import debug_toolbar

	urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),
				   path('view/', debug_view), ] + urlpatterns
