from django.utils.text import slugify
from django.db.models.signals import pre_save
from .models import Product
from django.dispatch import receiver
import random


@receiver(pre_save, sender=Product)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)
        if sender.objects.filter(slug=slug).exists():
            while sender.objects.filter(slug=slug).exists():
                text = slug.rstrip('1234567890')
                slug = text + "_" + slugify(random.random())
        instance.slug = slug
