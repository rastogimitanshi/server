# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-13 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyramid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppTOCExplainerMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('toc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyramid.AppTOC')),
            ],
            options={
                'ordering': ['order'],
                'db_table': 'web_apptocexplainermap',
                'verbose_name': 'Law Explainer',
                'verbose_name_plural': 'Law Explainers',
            },
        ),
        migrations.CreateModel(
            name='AppTOCHomeExplainerMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('toc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyramid.AppTOC')),
            ],
            options={
                'ordering': ['order'],
                'db_table': 'web_apptochomeexplainermap',
                'verbose_name': 'Law Explainers ( Home )',
                'verbose_name_plural': 'Law Explainers ( Home ) ',
            },
        ),
    ]