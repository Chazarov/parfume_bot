import requests
from typing import List
import json
from core.config import configs

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from catalogs.models import (Category, Brand, Product, SliderImges, ProductImage, 
                             Cart, CartItem, PriceVolumeItem, RunningLine, Settings)
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404


def start_page(request):
    categories = Category.objects.all()
    slides = SliderImges.objects.all()
    slides_count = len(slides)
    range_slides = range(slides_count)
    running_line = RunningLine.objects.all().first()
    running_line_text = running_line.text

    


    return render(request, 'catalogs/start.html', 
    {
        'categories':categories,
        'slides':slides,
        'range_slides':range_slides,
        'slides_count':slides_count,
        "running_line_text":running_line_text,
    })



def category_catalogs(request, category_id):
    category = Category.objects.get(id = category_id)
    return product_by_category(request, category_id)

    



def brands_catalog_by_category(request, category_id):
    brands = Brand.objects.filter(product__category_id=category_id).distinct()
    if(brands.exists()):
        return render(request, 'catalogs/brand_catalog.html', 
        {
            "brands": brands,
            "category_id": category_id,
        })
    else:
        return product_by_category(request, category_id=category_id)






def product_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    cart_items = CartItem.objects.filter(cart=request.cart)
    products_in_cart = [item.product.id for item in cart_items]
    products = Product.objects.filter(category__id = category_id)
    
    return render(request, 'catalogs/product_catalog.html',
    {
        "products":products,
        "title":category.name,
        "products_in_cart":products_in_cart
    })



def products_by_brend(request, brand_id):
    products = Product.objects.filter(brand__id = brand_id)
    brand = Brand.objects.get(id = brand_id)
    cart_items = CartItem.objects.filter(cart=request.cart)
    products_in_cart = [item.product.id for item in cart_items]

    return render(request, 'catalogs/product_catalog.html',
    {
        "products":products,
        "title":brand.name,
        "products_in_cart":products_in_cart,
    })


def product_by_brend_and_category(request,  brand_id, category_id):
    products = Product.objects.filter(brand__id = brand_id).filter(category__id = category_id)
    brand = Brand.objects.get(id = brand_id)
    category = Category.objects.get(id = category_id)

    
    cart_items = CartItem.objects.filter(cart=request.cart)
    products_in_cart = [item.product.id for item in cart_items]

    return render(request, 'catalogs/product_catalog.html',
    {
        "products":products,
        "title":f"{category.name} {brand.name}",
        "products_in_cart":products_in_cart,
    })



def product_page(request:WSGIRequest, product_id):
    product = Product.objects.get(id = product_id)
    images = product.images.all()
    images_count = len(images)
    range_images = range(len(images))
    cart_items = CartItem.objects.filter(cart=request.cart)
    products_in_cart = [item.product.id for item in cart_items]
    in_cart = product_id in products_in_cart

    return render(request, 'catalogs/product.html',{
        "product":product,
        "images":images,
        "range_images":range_images,
        "images_count":images_count,
        "in_cart":in_cart
    })


def cart_page(request):
    cart_items = list(request.cart.cartitem_set.all())
    return render(request, 'catalogs/cart_list.html',
    {
        "cart_items":cart_items,
    })



def add_to_cart_or_delete_in_cart(request: WSGIRequest):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            volume_item_id = data.get('volume_item_id')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        

        cart = request.cart
        product = Product.objects.get(id=product_id)
        if(not volume_item_id):
            cart_items = CartItem.objects.filter(cart = cart, product=product)
            if(cart_items.exists()):
                cart_items.delete()
                return JsonResponse({'in_cart': False}, status=200)
            else:
                price_volume_item = PriceVolumeItem.objects.filter(product=product).first()
                CartItem.objects.create(cart = cart, product = product, price_item = price_volume_item)
                return JsonResponse({'in_cart': True}, status=200)
        else:
            price_volume_item = PriceVolumeItem.objects.get(id = volume_item_id)

            try:
                cart_item = CartItem.objects.get(cart = cart, product = product, price_item = price_volume_item)
                cart_item.delete()
                return JsonResponse({'in_cart': False}, status=200)
            except CartItem.DoesNotExist:
                CartItem.objects.create(cart = cart, product = product, price_item = price_volume_item)
                return JsonResponse({'in_cart': True}, status=200)

    else:
        return JsonResponse({'error': 'Invailid request method'}, status=400)




def product_is_in_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            volume_item_id = data.get('volume_item_id')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        

        cart = request.cart
        product = Product.objects.get(id=product_id)
        if(not volume_item_id):
            cart_items = CartItem.objects.filter(cart = cart, product=product)
            if(cart_items.exists()):
                return JsonResponse({'in_cart': True}, status=200)
            else:
                return JsonResponse({'in_cart': False}, status=200)
        else:
            price_volume_item = PriceVolumeItem.objects.get(id = volume_item_id)
            try:
                CartItem.objects.get(cart = cart, product = product, price_item = price_volume_item)
                return JsonResponse({'in_cart': True}, status=200)
            except CartItem.DoesNotExist:
                return JsonResponse({'in_cart': False}, status=200)

    else:
        return JsonResponse({'error': 'Invailid request method'}, status=400)



def get_cart_counter(request):
    cart_items = list(request.cart.cartitem_set.all())
    counter = len(cart_items)
    return JsonResponse({'counter': counter})


def get_price(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            volume_item_id = data.get('volume_item_id')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        

        try:
            price_volume_item = PriceVolumeItem.objects.get(id = volume_item_id)
            return JsonResponse({'price': price_volume_item.price}, status=200)
        except: 
            return JsonResponse({'error': 'Not Found price item'}, status=405)

    else:
        return JsonResponse({'error': 'Invailid request method'}, status=400)



def to_help(request):
    settings = Settings.objects.all().first()
    url = settings.help_url
    
    return HttpResponseRedirect(url)

def to_bot(request):
    settings = Settings.objects.all().first()
    url = settings.bot_url
    
    return HttpResponseRedirect(url)

def to_channel(request):
    settings = Settings.objects.all().first()
    url = settings.main_channel_url
    
    return HttpResponseRedirect(url)




def process_order(request: WSGIRequest):

    bot_api = configs.BOT_API_URL

    settings = Settings.objects.all().first()
    admin_id = settings.admin_id
    
    cart: Cart = request.cart
    telegram_id = request.GET.get('tgUserId')  
    username = request.GET.get('username')


    cart_items = []
    for cart_item in CartItem.objects.filter(cart=cart):
        cart_items.append({
            'product_id': cart_item.product.id,
            'name': cart_item.product.name,
            'price': cart_item.price_item.price,
            'volume': cart_item.price_item.volume,
        })

    
    if not telegram_id:
        return JsonResponse({'error': 'Telegram ID not provided'}, status=400)

    response = requests.post(bot_api, json={
        'admin_id':admin_id,
        'telegram_id': telegram_id,
        'username': username,
        'cart': cart_items
    })

    error = response.json.get("error")
    

    
    if response.status_code == 200:
        return JsonResponse({'status': 'success'})
    else:
        print(f"❗❗❗  {response.text}  {error}   ❗❗❗")
        return JsonResponse({'status': 'failure', 'details': f"{response.text}  {error}"}, status=response.status_code)
    