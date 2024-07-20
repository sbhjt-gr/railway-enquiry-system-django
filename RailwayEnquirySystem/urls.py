"""RailwayEnquirySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('admin/', admin.site.urls, name = "admin"),
    path('test-page/', views.testpage, name = "testpage"),
    path('contact/', views.contact, name = "contact"),
    path('search/', views.search, name = "search"),
    path('results/', views.s_result, name = "results"),
    path('pnr/', views.pnr, name = 'pnr'),
    path('pnr-search/', views.pnr_search, name = 'pnr-result'),
    path('station/', views.station, name = "station"),
    path('station-search/', views.station_result, name = 'station-results'),
    path('about/', views.about, name = 'about')
]
