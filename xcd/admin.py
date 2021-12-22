from django.contrib import admin
from .models import Format, Samples, Style


class FormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class SamplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'authors', 'title', 'size', 'published')
    list_display_links = ('id', 'authors')
    search_fields = ('title', 'authors')
    list_editable = ('published',)
    list_filter = ('published', 'authors')


admin.site.register(Format, FormatAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Samples, SamplesAdmin)
