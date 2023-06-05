from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='наименование')
    translator = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name} {self.translator}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='наименование')
    translator = models.TextField(verbose_name='описание')
    product_image = models.ImageField(upload_to='product/', verbose_name='изображение', null=True, blank=True)
    product_category_name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(verbose_name='дата создания')
    date_last_change = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.product_category_name}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов
