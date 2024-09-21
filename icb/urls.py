"""
URL configuration for icb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import p

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',p.web1,name='signin'),
    path('login/',p.web2,name='login'),
    path('user/',p.web3,name='user'),
    path('business/',p.web4,name='business'),
    path('investor/',p.web5,name='investor'),
    path('banker/',p.web6,name='banker'),
    path('businessadviser/',p.web7,name='businessadviser'),
    path('home/',p.web8,name='home'),
    path('idea/',p.web10,name='idea'),
    path('isign/',p.web11,name='isign'),
    path('ilog/',p.web12,name='ilog'),
    path('bsign/',p.web13,name='bsign'),
    path('blog/',p.web14,name='blog'),
    path('basign/',p.web15,name='basign'),
    path('balog/',p.web16,name='balog'),
    path('ilist/',p.web17,name='ilist'),
    path('blist/',p.web18,name='blist'),
    path('balist/',p.web19,name='balist'),
    path('list/',p.web20,name='list'),
    
]
