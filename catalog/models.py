from django.db import models
from django.utils import timezone

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    overview = models.TextField(max_length=255, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    overview = models.TextField(max_length=255, verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_update = models.DateTimeField(default=None, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.overview} {self.preview} {self.category} {self.price} {self.date_of_creation} ' \
               f'{self.last_update}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def save(self, *args, **kwargs):
        if self.pk:
            self.last_update = timezone.now()
        super(Product, self).save(*args, **kwargs)
