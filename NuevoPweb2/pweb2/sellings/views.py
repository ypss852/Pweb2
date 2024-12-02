from django.shortcuts import render, redirect
from .models import Selling
from .forms import SellingForm

def selling_list(request):
    sellings = Selling.objects.all()
    return render(request, 'sellings/selling_list.html', {'sellings': sellings})

def selling_create(request):
    if request.method == 'POST':
        form = SellingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selling_list')
    else:
        form = SellingForm()
    return render(request, 'sellings/selling_form.html', {'form': form})
