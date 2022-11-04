from django.db import models
from django.contrib.auth.models import User


class TestUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="test_user")
    category = models.ManyToManyField(to='Category', blank=True)
    amount = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    organisation = models.ForeignKey(to='Organisation', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)


class Organisation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
