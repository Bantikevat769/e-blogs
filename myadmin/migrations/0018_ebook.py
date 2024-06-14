# Generated by Django 5.0.2 on 2024-05-23 15:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0017_delete_ebook'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('file', models.FileField(upload_to='ebooks/')),
                ('users', models.ManyToManyField(blank=True, related_name='purchased_ebooks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]