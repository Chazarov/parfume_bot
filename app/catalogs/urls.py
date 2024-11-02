from django.urls import path
from catalogs import views

urlpatterns = [
    path('', views.start_page, name = "start"),
    path('brands', views.brands_page, name = "brands"),
    path('products', views.products_page, name = "products")
]
