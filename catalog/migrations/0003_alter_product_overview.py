# Generated by Django 4.2.4 on 2023-08-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='overview',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
    ]