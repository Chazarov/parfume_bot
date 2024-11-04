from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from catalogs.models import Category, Brand, Product, SliderImges, ProductImage, Cart, CartItem
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404


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
    cart_items = CartItem.objects.filter(cart=request.cart)
    products_in_cart = [item.product.id for item in cart_items]


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
        "primary":prime_category,
        "products_in_cart":products_in_cart
    })



def product_page(request:WSGIRequest, product_id):
    
    product = Product.objects.get(id = product_id)
    images = product.images.all()
    images_count = len(images)
    range_images = range(len(images))
    cart_items = CartItem.objects.filter(cart=request.cart)
    products_in_cart = [item.product.id for item in cart_items]
    in_cart = product in products_in_cart

    print(images[0].image.url)

    return render(request, 'catalogs/product.html',
    {
        "product":product,
        "images":images,
        "range_images":range_images,
        "images_count":images_count,
        "in_cart":in_cart
    })


def add_product(request:WSGIRequest, product_id):

    product = Product.objects.get(id = product_id)
    if(request.method == 'GET'):
        if('add_product' in request.GET):
            print("add product❗❗❗")
            cart_item, created = CartItem.objects.get_or_create(product=product, cart=request.cart)
    
        return HttpResponse("Product successfully added to cart")
    else:
        return HttpResponseBadRequest("Invalid request method or missing 'add_product'")


def remove_product(request: WSGIRequest, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'GET' and 'remove_product' in request.GET:
        # Ищем CartItem, соответствующий продукту и корзине
        cart_item = CartItem.objects.filter(cart=request.cart, product=product).first()
        if cart_item:
            cart_item.delete()  # Удаляем товар из корзины
            return HttpResponse("Product successfully remove from cart")
        else:
            return HttpResponseBadRequest("Product not found in cart")
    else:
        return HttpResponseBadRequest("Invalid request method or missing 'remove_product'")