from django.contrib.sessions.middleware import MiddlewareMixin
from django.http import HttpRequest
from .models import Cart

class CartMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart_id = request.session.get('cart_id')
            if cart_id:
                try:
                    cart = Cart.objects.get(id=cart_id)
                except Cart.DoesNotExist:
                    cart = Cart.objects.create()
                    request.session['cart_id'] = cart.id
            else:

                delete_unused_backets()

                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        
        request.cart = cart


def delete_unused_backets():
    Cart.objects.filter(items__isnull=True).delete()