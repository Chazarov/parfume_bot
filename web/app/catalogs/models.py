from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField("Название", max_length=55)
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name




class Brand(models.Model):
    name = models.CharField("Название", max_length=55)
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='brand_images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name




class ProductType(models.Model):
    name = models.CharField("Тип продукта", max_length=25)

    def __str__(self):
        return self.name

    

class Product(models.Model):
    name = models.CharField("Название", max_length=55)
    description = models.TextField("Описание", blank=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.CharField("Страна производитель", default="неизвестно", max_length=55)
    type_of_product = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="product_type")

    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name    
    

class PriceVolumeItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="price_volume_items")
    price = models.IntegerField("Цена", default=0)
    volume = models.IntegerField("Объем", default=0)

    def __str__(self):
        return f"{self.product} {self.volume}"  



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
    brand = models.ForeignKey(Brand , null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Баннеры стартового слайдера"

    def __str__(self):
        return self.title
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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
    price_item = models.ForeignKey(PriceVolumeItem, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Позиции корзины"
        unique_together = ('cart', 'product', 'price_item')  # Уникальность



class RunningLine(models.Model):
    text = models.TextField("Текст бегущей строки", default=" - ")

    class Meta:
        verbose_name_plural = "Бегущая строка"

    def __str__(self):
        return self.text.__str__()
    

class Settings(models.Model):
    name = models.CharField(" - ", max_length=50, default="Настройки", blank=True)


    admin_id = models.BigIntegerField("Telegram Id (менеджер)", null=True, blank=True, default=None)
    main_channel_url = models.CharField("ссылка основного телеграм канала", default=" ", max_length=255, blank=True)
    help_url = models.CharField("ссылка поддержки", default=" ", max_length=255, blank=True)
    bot_url = models.CharField("ссылка бота", default=" ", max_length=255, blank=True)


    class Meta:
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.name.__str__()

