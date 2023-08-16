from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    overview = models.TextField(max_length=255, verbose_name='Описание')
    preview = models.ImageField(upload_to='media/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=255, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания')
    last_update = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.overview} {self.preview} {self.category} {self.price} {self.date_of_creation} ' \
               f'{self.last_update}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    overview = models.TextField(max_length=255, verbose_name='Описание')
    created_at = models.DateTimeField

    def __str__(self):
        return f'{self.name} {self.overview} {self.created_at}'

    class Meta:
        verbose_name = 'Категория'
