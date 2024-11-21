from django.db.models.signals import post_delete
from django.db.models.signals import post_migrate

from django.dispatch import receiver
from django.contrib.sessions.models import Session

from catalogs.models import Cart
from catalogs.models import RunningLine






@receiver(post_migrate)
def post_migrate_handler(sender, **kwargs):
    o = RunningLine.objects.all()
    if(not o.exists()):
        RunningLine.objects.create()
    


# Сигнал срабатывает при удалении записи сессии
@receiver(post_delete, sender=Session)
def session_ended(sender, instance, **kwargs):
    try:
        instance.cart.delete()
    except:
        Exception("cart instanse not found")
    print(f"Сессия с ID {instance.session_key} была завершена")