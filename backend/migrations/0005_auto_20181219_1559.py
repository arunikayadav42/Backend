# Generated by Django 2.1 on 2018-12-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20181218_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charts',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
