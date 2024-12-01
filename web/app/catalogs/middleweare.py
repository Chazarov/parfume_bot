import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.sessions.middleware import MiddlewareMixin
from django.http import HttpRequest
from .models import Cart

class CartMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        # Проверяем, если пользователь аутентифицирован
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            # Если анонимный пользователь, пытаемся получить токен из заголовков
            token = request.headers.get('Authorization')
            if token and token.startswith('Bearer '):
                token = token.split(' ')[1]  # Извлекаем токен из заголовка

                try:
                    # Декодируем токен и извлекаем данные
                    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                    # Получаем cart_id или другой идентификатор из токена
                    cart_id = payload.get('cart_id')

                    if cart_id:
                        # Ищем корзину по id, если токен валиден
                        try:
                            cart = Cart.objects.get(id=cart_id)
                        except Cart.DoesNotExist:
                            # Если корзина не найдена, создаем новую
                            cart = Cart.objects.create()
                    else:
                        # Если cart_id отсутствует в токене, создаем новую корзину
                        cart = Cart.objects.create()

                except jwt.ExpiredSignatureError:
                    # Если токен истек, создаем новую корзину
                    cart = Cart.objects.create()
                except jwt.InvalidTokenError:
                    # Если токен неверный, создаем новую корзину
                    cart = Cart.objects.create()

                # Сохраняем cart_id в сессии, чтобы можно было использовать при следующем запросе
                request.session['cart_id'] = cart.id
            else:
                # Если нет токена, проверяем cart_id в сессии
                cart_id = request.session.get('cart_id')
                if cart_id:
                    try:
                        cart = Cart.objects.get(id=cart_id)
                    except Cart.DoesNotExist:
                        cart = Cart.objects.create()
                        request.session['cart_id'] = cart.id
                else:
                    # Если cart_id нет в сессии, создаем новую корзину
                    cart = Cart.objects.create()
                    request.session['cart_id'] = cart.id

        # Сохраняем корзину в запросе
        request.cart = cart