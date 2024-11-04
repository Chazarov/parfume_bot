from django.urls import path
from catalogs import views

urlpatterns = [
    path('', views.start_page, name = "start"),
    path('category/<int:category_id>/', views.brands_page, name = "brands"),
    path('category/<int:category_id>/brand/<int:brand_id>/', views.products_page, name = "products"),
    path('<int:product_id>/', views.product_page, name = "product")
]




requests = [
    path('api/add_product/<int:product_id>', views.add_product, name='add_product_in_cart'),
    path('api/remove_product/<int:product_id>', views.remove_product, name='add_product_in_cart')
]


urlpatterns += requests


