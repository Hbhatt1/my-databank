# Generated by Django 2.1 on 2018-09-18 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databank', '0016_auto_20180910_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='squamcont',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='result',
            name='tcc',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='result',
            name='viability',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
