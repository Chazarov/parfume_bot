from django.urls import path
from catalogs import views

urlpatterns = [
    path('', views.start_page, name = "start"),
    path('category/<int:category_id>/', views.brands_page, name = "brands"),
    path('category/<int:category_id>/brand/<int:brand_id>/', views.products_page, name = "products"),
    path('<int:product_id>/', views.product_page, name = "product"),
]




requests = [
    path('api/add_product/<int:product_id>', views.add_product, name='add_product_in_cart'),
    path('api/remove_product/<int:product_id>', views.remove_product, name='remove_product_in_cart'),
    path('api/cart', views.get_cart, name='get_cart'),
    path('api/help', views.get_help, name='get_help'),
    path('api/process_order', views.process_order, name='process_order'),
]


urlpatterns += requests


