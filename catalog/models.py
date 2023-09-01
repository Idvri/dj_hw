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
    last_update = models.DateTimeField(default=None, verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def save(self, *args, **kwargs):
        if self.pk:
            self.last_update = timezone.now()
        super(Product, self).save(*args, **kwargs)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(default=0, verbose_name='Номер версии')
    version_name = models.CharField(max_length=255, verbose_name='Название версии')
    is_current = models.BooleanField(default=False, verbose_name='Признак активности версии')

    def __str__(self):
        return f'Номер версии: {self.version_number}; Название версии: {self.version_name}.'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
