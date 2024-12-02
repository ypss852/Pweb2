from django.urls import path
from . import views

urlpatterns = [
    path('', views.selling_list, name='selling_list'),
    path('create/', views.selling_create, name='selling_create'),
]

