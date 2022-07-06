# Generated by Django 4.0.4 on 2022-07-06 13:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockMarket', '0008_alter_portafolio_country_alter_stock_ticker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portafolio',
            name='user',
        ),
        migrations.AddField(
            model_name='portafolio',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
