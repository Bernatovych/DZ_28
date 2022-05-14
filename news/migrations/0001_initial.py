# Generated by Django 3.2.13 on 2022-05-13 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(unique=True, verbose_name='Website url')),
                ('element', models.CharField(max_length=50, verbose_name='Element(div, p , li ....)')),
                ('attribute', models.CharField(blank=True, max_length=50, verbose_name='Attribute(id, class)')),
                ('value', models.CharField(blank=True, max_length=50, verbose_name='Attribute value')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Url')),
                ('title', models.TextField(verbose_name='Title')),
                ('website_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news.websitesettings')),
            ],
        ),
    ]
