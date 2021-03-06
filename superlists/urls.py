"""superlists URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from lists import views as lv

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', lv.home_page, name='home'),
	url(r'^lists/(\d+)/$', lv.view_list, name='view_list'),
	url(r'^lists/new$', lv.new_list, name='new_list'),
	url(r'^lists/(\d+)/add_item$', lv.add_item, name='add_item'),
]
