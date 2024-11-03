from django.shortcuts import render
from catalogs.models import Category, Brand, Product, SliderImges, ProductImage


def start_page(request):

    categories = Category.objects.all()
    images = SliderImges.objects.all()
    images_count = len(images)
    range_images = range(images_count)
    


    return render(request, 'catalogs/start.html', 
    {
        'categories':categories,
        'images':images,
        'range_images':range_images,
        'images_count':images_count
    })



def brands_page(request, category_id):

    category = Category.objects.get(id = category_id)
    if(category.prime_category):
        return products_page(request, None, category_id, prime_category=True)

    brands = Brand.objects.all()

    return render(request, 'catalogs/brand_catalog.html', 
    {
        "brands":brands, 
        "category_id":category_id,
    })



def products_page(request, brand_id, category_id, prime_category:bool=False):


    category = None
    brand = None
    category = Category.objects.get(id=category_id)
    if(not prime_category):
        products = Product.objects.filter(brand__id = brand_id).filter(category__id = category_id)
        brand = Brand.objects.get(id = brand_id)
    else:
        products = Product.objects.filter(category__id = category_id)


    return render(request, 'catalogs/product_catalog.html',
    {
        "products":products,
        "category":category,
        "band":brand,
        "primary":prime_category
    })



def product_page(request, product_id):
    
    product = Product.objects.get(id = product_id)
    images = product.images.all()
    images_count = len(images)
    range_images = range(len(images))

    print(images[0].image.url)

    return render(request, 'catalogs/product.html',
    {
        "product":product,
        "images":images,
        "range_images":range_images,
        "images_count":images_count
    })