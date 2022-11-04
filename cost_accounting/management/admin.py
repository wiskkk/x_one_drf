from django.contrib import admin
from django.contrib.admin import register

from .models import Transaction, Category, TestUser


@register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ('amount', 'category', 'updated_at', "category", "organisation", "description")


@register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)


@register(TestUser)
class TestUser(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('category',)
