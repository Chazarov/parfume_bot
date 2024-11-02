from django.shortcuts import render


def start_page(request):
    return render(request, 'catalogs/start.html')

def brands_page(request):
    return render(request, 'catalogs/brand_catalog.html')

def products_page(request):
    return render(request, 'catalogs/product_catalog.html')

def user_page(request):
    pass