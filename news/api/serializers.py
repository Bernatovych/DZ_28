from rest_framework import serializers
from news.models import News, WebsiteSettings


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['website_settings', 'url', 'title']


class WebsiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteSettings
        fields = ['website', 'element', 'attribute', 'value']