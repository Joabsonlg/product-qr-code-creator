# Generated by Django 3.2.9 on 2021-11-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_alter_product_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='shop',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]