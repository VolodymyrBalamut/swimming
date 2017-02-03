# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-24 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_swimmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_time', models.CharField(max_length=20)),
                ('competition', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('location_city', models.CharField(max_length=20)),
                ('distance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Distance')),
                ('location_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Country')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Style')),
                ('swimmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Swimmer')),
            ],
            options={
                'db_table': 'records',
            },
        ),
    ]