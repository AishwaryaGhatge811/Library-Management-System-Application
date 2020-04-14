from django.contrib import admin
from django.urls import path,include
from. import views


urlpatterns = [
    path('',views.home),
    path('addition',views.addition),
    path('subtraction', views.subtraction),
    path('multiplication', views.multiplication),
    path('division', views.division),
]