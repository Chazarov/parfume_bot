from django.utils.deprecation import MiddlewareMixin
from django.core.handlers.wsgi import WSGIRequest
from catalogs.models import Cart

class CartMiddleware(MiddlewareMixin):
    def process_request(self, request:WSGIRequest):


        if request.user.is_authenticated:
            # Получаем или создаем корзину для авторизованного пользователя
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            # Для анонимных пользователей используем сессию
            cart_id = request.session.get('cart_id')
            if cart_id:
                # Если корзина уже есть в сессии
                try:
                    cart = Cart.objects.get(id=cart_id)
                except Cart.DoesNotExist:
                    # Если корзина по id не найдена, создаем новую
                    cart = Cart.objects.create()
                    request.session['cart_id'] = cart.id
            else:
                # Создаем новую корзину и сохраняем её в сессии
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        
        # Сохраняем корзину в запросе для доступа в представлениях
        request.cart = cart