from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='название товара')
    describe = models.TextField(verbose_name='описание товара')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100)
    cost = models.IntegerField(verbose_name='стоимость товара', default=100)
    date_create = models.DateTimeField(verbose_name='дата создания', default=timezone.now)
    last_update = models.DateTimeField(verbose_name='дата последнего обновления', default=timezone.now)

    def __str__(self):
        return f'{self.name} {self.describe} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название категории')
    describe = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.name} {self.describe}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
