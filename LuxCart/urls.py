"""Stackup URL Configuration

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
    path('',views.home,name='home'),
    path('search/products/', views.search_products, name='search_products'),
    path('search/', views.home, name='search'),
    path('detail/<int:id>/',views.pd,name='pd'),
    path('cart/add/<int:id>/', views.add_cart, name='add_cart'),
    path('cart/delete/<int:id>/', views.delete_cart, name='delete_cart'),
    path('cart/',views.cart,name='cart'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutview,name='logout')

]
