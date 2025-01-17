# Generated by Django 5.0.2 on 2024-05-13 04:59

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_blog_alter_subcategory_cat_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='main_post',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='section',
            field=models.CharField(choices=[('Popular', 'Popular'), ('Recent', 'Recent'), ('Editor_Pick', 'Editor_Pick'), ('Tranding', 'Tranding'), ('Inspiration', 'Inspiration'), ('Latest_Posts', 'Latest_Posts')], default='Popular', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('0', 'Draft'), ('1', 'Publish')], default='Draft', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.category'),
        ),
    ]
