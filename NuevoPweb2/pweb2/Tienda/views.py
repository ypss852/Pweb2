from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a Tienda</h1><p>Explora los productos y ventas.</p>")
