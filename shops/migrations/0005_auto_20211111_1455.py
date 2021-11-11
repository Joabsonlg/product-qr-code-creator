# Generated by Django 3.2.9 on 2021-11-11 17:55

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_remove_shop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]