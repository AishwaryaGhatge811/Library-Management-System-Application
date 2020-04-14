from django.contrib import admin
from django.urls import path,include
from. import views


urlpatterns = [
    path('',views.login_page),
    path('login_page', views.login_page),
    path('add_book', views.add_book),
    path('update_book', views.update_book),
    path('search_book', views.search_book),
    path('delete_book', views.delete_book),
    path('view_book', views.view_book),
    path('log_out',views.log_out),
    path('register', views.register),

]