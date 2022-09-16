# Generated by Django 2.2 on 2022-04-26 14:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]
