from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Samples(models.Model):
    author = models.ManyToManyField('Author', verbose_name='Автор')
    style = models.ManyToManyField('Style', verbose_name='Стиль')
    format = models.ManyToManyField('Format', verbose_name='Формат')
    title = models.CharField(max_length=50, verbose_name='Название семплов')
    descriptions = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    size = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Размер в MB')
    link = models.TextField(verbose_name='Ссылка на сачивание файлов')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Семплы'
        verbose_name_plural = 'Семплы'


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):  # автоматически заполнить поле slug при добавлении автора
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        unique_together = 'name',  # уникальное имя
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class Style(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название стиля')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('style', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'
        ordering = ['name']


class Format(models.Model):
    name = models.CharField(max_length=50, verbose_name='Формат семплов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'
        ordering = ['name']
