# Generated by Django 4.1 on 2023-01-27 23:47

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_date_published'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 27, 23, 47, 8, 998355, tzinfo=datetime.timezone.utc)),
        ),
    ]
