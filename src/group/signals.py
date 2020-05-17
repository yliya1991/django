from django.db.models.signals import pre_save
from django.dispatch import receiver

from group.models import Group


@receiver(pre_save, sender=Group)
def group_capitalize(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
