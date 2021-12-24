from django.contrib import admin
from .models import Format, Samples, Style, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class FormatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SamplesAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'published')
    search_fields = ('title', 'size',)
    list_editable = ('published',)
    list_filter = ('published', 'authors',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Samples, SamplesAdmin)
