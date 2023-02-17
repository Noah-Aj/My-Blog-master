# Generated by Django 4.1 on 2023-01-28 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_blog_img_alter_post_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_slug_title',
            field=models.SlugField(max_length=200, unique=True, unique_for_date='date_published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 13, 45, 2, 730122, tzinfo=datetime.timezone.utc)),
        ),
    ]