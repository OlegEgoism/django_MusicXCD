from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class FormatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SamplesAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'size', 'created', 'get_photo',)
    search_fields = ('title',)
    list_editable = ('published',)
    list_filter = ('published', 'author',)

    def get_photo(self, result_list):
        if result_list.photo:
            return mark_safe(f'<img src="{result_list.photo.url}" width="40">')
        else:
            return 'Нет фото'

    get_photo.short_description = 'Изображение'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Samples, SamplesAdmin)
