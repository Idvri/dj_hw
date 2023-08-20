# Generated by Django 4.2.4 on 2023-08-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('overview', models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('overview', models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена за покупку')),
                ('date_of_creation', models.DateTimeField(verbose_name='Дата создания')),
                ('last_update', models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
