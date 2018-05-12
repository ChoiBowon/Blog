from django.urls import path,include
from . import views
from django.contrib import admin

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='list'),
    path('<int:blog_id>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
]