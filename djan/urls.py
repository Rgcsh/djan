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
from django.urls import include, path
from django.urls import re_path

from rgc.views import index, reg, new_reg, new_reg1, register, debug_view, export, post

urlpatterns = [
	path('admin/', admin.site.urls),
	path('hello/', index),
	re_path('^reg/$', reg),
	path('new_reg/<int:a>/<int:b>/', new_reg),
	path('new_reg1/', new_reg1),
	path('register/', register),
	path('export/', export),
	path('post/', post),
]

if settings.DEBUG:
	import debug_toolbar

	urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),
				   path('view/', debug_view), ] + urlpatterns
