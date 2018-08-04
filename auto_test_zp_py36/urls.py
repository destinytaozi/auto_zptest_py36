"""auto_test_zp_py36 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from aha_test4dj import views

urlpatterns = [
    path('^admin/', admin.site.urls),
    url(r'^index/',views.index),
    url(r'^$/',views.index),
    url(r'^account/login/$',views.index),
    url(r'^event_manage/$',views.event_manage),
    url(r'^login_action/$',views.login_action),
]
