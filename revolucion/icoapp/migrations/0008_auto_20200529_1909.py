# Generated by Django 3.0.4 on 2020-05-29 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icoapp', '0007_auto_20200529_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ico',
            old_name='period',
            new_name='days',
        ),
    ]
