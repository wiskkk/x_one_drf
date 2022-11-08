from django.contrib import admin
from django.contrib.admin import register

from .models import Transaction, Category


@register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ('amount', 'category', 'updated_at', "category", "organisation", "description")


@register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
