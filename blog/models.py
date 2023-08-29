from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, verbose_name='URL', unique=True, blank=True)
    overview = models.TextField(max_length=255, verbose_name='Cодержимое', **NULLABLE)
    preview = models.ImageField(upload_to='media/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_counter = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def generate_slug(self):
        slug = self.title.lower().replace(" ", "-")
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
