# Generated by Django 3.0.4 on 2020-05-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icoapp', '0004_remove_ico_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ico',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
