# Generated by Django 4.0.4 on 2022-06-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockMarket', '0005_delete_chessboard_remove_portafoliouser_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='portafolio',
            name='tags',
        ),
        migrations.AddField(
            model_name='portafolio',
            name='userStock',
            field=models.ManyToManyField(to='stockMarket.stock'),
        ),
    ]