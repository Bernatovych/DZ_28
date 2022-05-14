from django.contrib import admin
from .models import WebsiteSettings, News


@admin.register(WebsiteSettings)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('website', 'element', 'attribute', 'value')
    list_filter = ('website',)


@admin.register(News)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('website_settings', 'url', 'title')
    list_filter = ('website_settings', 'title')
