# Generated by Django 5.0.2 on 2024-05-22 10:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0013_ebook'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='purchased_by',
            field=models.ManyToManyField(related_name='purchased_ebooks', to=settings.AUTH_USER_MODEL),
        ),
    ]
