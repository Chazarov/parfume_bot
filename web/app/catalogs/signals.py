from django.db.models.signals import post_delete
from django.db.models.signals import post_migrate

from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model

from catalogs.models import Cart, RunningLine, Settings

from core.config import configs






@receiver(post_migrate)
def post_migrate_handler(sender, **kwargs):


    o = RunningLine.objects.all()
    if(not o.exists()):
        RunningLine.objects.create()

    o = Settings.objects.all()
    if(not o.exists()):
        Settings.objects.create()

    if(configs.SUPERUSER_NAME and configs.SUPERUSER_PASS and configs.SUPERUSER_EMAIL):
        User = get_user_model()  
        User.objects.filter(username='admin').exists() or \
        User.objects.create_superuser(configs.SUPERUSER_NAME, configs.SUPERUSER_EMAIL, configs.SUPERUSER_PASS)


    
    
    


# Сигнал срабатывает при удалении записи сессии
@receiver(post_delete, sender=Session)
def session_ended(sender, instance, **kwargs):
    try:
        instance.cart.delete()
    except:
        Exception("cart instanse not found")
    print(f"Сессия с ID {instance.session_key} была завершена")