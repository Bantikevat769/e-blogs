# Generated by Django 5.0.2 on 2024-05-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0018_ebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]