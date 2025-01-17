# Generated by Django 5.0.2 on 2024-05-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0015_delete_ebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
