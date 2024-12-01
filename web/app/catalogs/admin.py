from django.contrib import admin
from catalogs.models import (ProductType ,Category, 
                             Brand, Product, SliderImges, 
                             Cart, CartItem, ProductImage, 
                             PriceVolumeItem, RunningLine, Settings)





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


class ProductVolumeItemInline(admin.TabularInline):
    model = PriceVolumeItem
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductVolumeItemInline]
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    


@admin.register(ProductType)
class Type(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(SliderImges)
class SliderImagesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)




class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)

    def has_delete_permission(self, request, obj=None):
        return False 
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(RunningLine)
class RunningLineAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False 

    def has_delete_permission(self, request, obj=None):
        return False 
    
    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)

    
    def has_add_permission(self, request, obj=None):
        return False 

    def has_delete_permission(self, request, obj=None):
        return False 
    
    def has_change_permission(self, request, obj=None):
        return True












