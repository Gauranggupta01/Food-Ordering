from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required

# Only logged-in users can access the product list
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Also protect product_detail view if needed
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
