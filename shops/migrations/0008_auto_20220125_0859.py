# Generated by Django 3.2.9 on 2022-01-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_alter_product_base_64_qr_code_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
