# Generated by Django 4.1.3 on 2022-11-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_category_name'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='category',
            field=models.ManyToManyField(blank=True, to='management.category'),
        ),
    ]
