from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category
from users.models import MyUser


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        category = Category.objects.filter(standard_category=True)
        user = MyUser.objects.get(id=instance.id)
        user.category.set(category)
