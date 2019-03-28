from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import perfiles


@receiver(post_save, sender=User)
def create_perfil(sender, instance, created, **kwargs):
    if created:
        perfiles.objects.create(user=instance)

@receiver(post_save, sender=User)
def savee_perfil(sender, instance, **kwargs):
    instance.perfiles.save()