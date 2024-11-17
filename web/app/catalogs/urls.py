from django.urls import path
from catalogs import views

urlpatterns = [
    path('', views.start_page, name = "start"),
    path('category/<int:category_id>/', views.brands_catalog_by_category, name = "brands"),
    path('category/<int:category_id>/brand/<int:brand_id>/', views.product_by_brend_and_category, name = "products"),
    path('cart', views.cart_page, name='cart'),
    path('<int:product_id>/', views.product_page, name = "product"),
    path('brand/<int:brand_id>/', views.products_by_brend, name = "brand_products"),
    path('help', views.get_help, name='get_help'),
    path('tgbot', views.to_bot, name = "bot")
]




requests = [
    path('api/cart/counter', views.get_cart_counter, name='get_cart_counter'),
    path('api/process-order', views.process_order, name='process_order'),
]

post = [
    path('api/cart/add-or-delete', views.add_to_cart_or_delete_in_cart, name='add_to_cart_or_delete'),
    path('api/cart/check', views.product_is_in_cart, name='check_in_cart'),
    path('api/product/price-items/get-price', views.get_price, name='get_price'),
]


urlpatterns += requests
urlpatterns += post


