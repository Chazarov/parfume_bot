from django.contrib import admin
from catalogs.models import Category, Brand, Product, SliderImges, Cart, CartItem, ProductImage



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product',)
    search_fields = ('product',)
    list_filter = ('product',)





@admin.register(SliderImges)
class SliderImagesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product',)
    search_fields = ('product',)
    list_filter = ('product',)









