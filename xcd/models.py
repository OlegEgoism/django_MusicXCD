from django.db import models


class Samples(models.Model):
    authors = models.ManyToManyField('Author', verbose_name='Автор')
    style = models.ManyToManyField('Style', verbose_name='Стиль')
    format = models.ManyToManyField('Format', verbose_name='Формат')
    title = models.CharField(max_length=50, verbose_name='Название')
    descriptions = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    size = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Размер в MB')
    link = models.TextField(verbose_name='Ссылка на сачивание файлов')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Семплы'
        verbose_name_plural = 'Семплы'


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Format(models.Model):
    name = models.CharField(max_length=50, verbose_name='Формат семплов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'


class Style(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название стиля')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'
