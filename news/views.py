from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from news.models import WebsiteSettings, News
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .tasks import pars_task


def home(request):
    test = 'asasas'
    return render(request, 'home.html', {'test': test})


# def pars(request):
#     pars_task.delay()
#     return redirect('home')


def pars(request):
    website_settings = WebsiteSettings.objects.all()
    for site in website_settings:
        website = site.website
        page = requests.get(website)
        soup = BeautifulSoup(page.text, 'lxml')
        try:
            attribute = site.attribute
        except IndexError:
            attribute = ''
        try:
            value = site.value
        except IndexError:
            value = ''
        domain = urlparse(website).netloc
        news = soup.findAll(site.element, attrs={attribute: value})
        for i in news:
            try:
                url = i.find('a').get('href')
                valid_url = URLValidator()
                try:
                    valid_url(url)
                except ValidationError:
                    url = domain + url
                News.objects.get_or_create(website_settings=site, url=url, title=i.text)
            except AttributeError:
                pass


