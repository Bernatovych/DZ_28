from bs4 import BeautifulSoup
import requests
from celery.schedules import crontab
from celery.task import periodic_task
from news.models import WebsiteSettings, News
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


@periodic_task(run_every=(crontab(minute='*/15')), name="pars_task", ignore_result=True)
def pars_task():
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



