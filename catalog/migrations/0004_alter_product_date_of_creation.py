# Generated by Django 4.2.4 on 2023-08-31 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]