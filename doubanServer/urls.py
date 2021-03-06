"""doubanServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include,re_path

# 获取django参数settings.py
from django.conf import settings
from django.views.static import serve

from doubanServer.settings import  STATICFILES_DIRS


urlpatterns = [
    path('admin/', admin.site.urls),

    # include 函数导入 douban app的urls
    path('douban/',include('douban.urls')), 
    re_path(r'^static/(?P<path>.*)$',serve,{
        'document_root':STATICFILES_DIRS
    })
    
]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))
