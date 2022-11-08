from rest_framework import serializers

from management.models import Category

from users.models import MyUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'standard_category',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'amount',)
