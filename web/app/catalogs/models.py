from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField("Название", max_length=55)
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    prime_category = models.BooleanField("Локальная категория", default=False)

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name




class Brand(models.Model):
    name = models.CharField("Название", max_length=55)
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name



    

class Product(models.Model):
    name = models.CharField("Название", max_length=55)
    price = models.IntegerField("Цена", default=0)
    description = models.TextField("Описание")
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.CharField("Страна производитель", default="неизвестно", max_length=55)
    volumes = models.CharField("Объемы",  max_length=22)
    type_of_product = models.CharField("Вид товара",  max_length=22)

    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
    


    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/') 

    class Meta:
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return f"{self.product.name} Image"    
    




class SliderImges(models.Model):
    image = models.ImageField("Изображение", upload_to='product_images/', max_length=255)
    title = models.CharField("Описание", max_length=255)
    brand = models.ForeignKey(Brand , null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Баннеры стартового слайдера"

    def __str__(self):
        return self.title
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Product, through='CartItem')

    class Meta:
        verbose_name_plural = "Корзины"

    @property
    def is_empty(self):
        return not self.items.exists()
    
    @property
    def item_count(self):
        return len(list(self.items.all()))
    
    @property
    def item_count_short(self):
        l = len(list(self.items.all()))
        if(l > 9): return "9+"
        return l

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Позиции корзины"
