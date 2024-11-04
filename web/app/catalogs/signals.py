from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.sessions.models import Session

from catalogs.models import Cart

# Сигнал срабатывает при удалении записи сессии
@receiver(post_delete, sender=Session)
def session_ended(sender, instance, **kwargs):
    try:
        instance.cart.delete()
    except:
        Exception("cart instanse not found")
    print(f"Сессия с ID {instance.session_key} была завершена")