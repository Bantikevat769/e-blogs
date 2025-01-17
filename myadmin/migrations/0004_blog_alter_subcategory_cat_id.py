# Generated by Django 4.0.10 on 2023-10-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_alter_subcategory_subcategory_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(help_text='Post name', max_length=255)),
                ('post_title', models.CharField(help_text='Post title', max_length=255)),
                ('category_id', models.IntegerField()),
                ('subcategory_id', models.IntegerField()),
                ('details', models.CharField(help_text='Details', max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='upload/')),
                ('audio', models.FileField(blank=True, upload_to='audio/')),
            ],
            options={
                'db_table': 'tabblog',
            },
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='cat_id',
            field=models.IntegerField(),
        ),
    ]
