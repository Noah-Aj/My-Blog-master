# Generated by Django 4.1 on 2023-01-28 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_blog_slug_title_alter_post_date_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 17, 24, 53, 976123, tzinfo=datetime.timezone.utc)),
        ),
    ]