from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Producto, Compra, Venta
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')

@login_required
def perfil(request):
    usuario = request.user
    compras = Compra.objects.filter(usuario=usuario)
    return render(request, 'perfil.html', {'usuario': usuario, 'compras': compras})

@login_required
def comprar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if producto.stock > 0:
        cantidad = request.POST.get('cantidad', 1)
        cantidad = int(cantidad)
        
        if producto.stock >= cantidad:
            
            compra = Compra.objects.create(
                usuario=request.user,
                producto=producto,
                cantidad=cantidad,
            )
            
            
            venta = Venta.objects.create(
                cliente=request.user.username,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio,
                total=producto.precio * cantidad,
            )
            
            
            producto.stock -= cantidad
            producto.save()
            
            
            return redirect('perfil')
        else:
            
            return HttpResponse("No hay suficiente stock para completar la compra.")
    else:
        
        return HttpResponse("Este producto no está disponible.")