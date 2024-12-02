from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('sellings/', include('sellings.urls')),
    path('', home, name='home'),  # Ruta para la página de inicio
]
