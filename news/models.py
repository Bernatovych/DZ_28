from django.db import models


class WebsiteSettings(models.Model):
    website = models.URLField(verbose_name='Website url', unique=True)
    element = models.CharField(max_length=50, verbose_name='Element(div, p , li ....)')
    attribute = models.CharField(max_length=50, verbose_name='Attribute(id, class)', blank=True)
    value = models.CharField(max_length=50, verbose_name='Attribute value', blank=True)

    def __str__(self):
        return self.website


class News(models.Model):
    website_settings = models.ForeignKey(WebsiteSettings, on_delete=models.CASCADE, related_name='news')
    url = models.URLField(verbose_name='Url')
    title = models.TextField(verbose_name='Title')

    def __str__(self):
        return self.title