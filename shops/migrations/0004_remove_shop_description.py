# Generated by Django 3.2.9 on 2021-11-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20211111_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='description',
        ),
    ]
