from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_usuario, name='registro'),     
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/profile/', views.perfil, name='perfil'),
    path('comprar/<int:producto_id>/', views.comprar_producto, name='comprar_producto'),
]