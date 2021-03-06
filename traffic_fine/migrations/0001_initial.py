# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-13 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import traffic_fine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficFine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traffic_offense', models.CharField(max_length=255)),
                ('simplified', models.TextField()),
                ('fine_first_offense', models.CharField(max_length=255)),
                ('jail_first_offense', models.CharField(blank=True, max_length=255)),
                ('fine_second_offense', models.CharField(blank=True, max_length=255)),
                ('jail_second_offense', models.CharField(blank=True, max_length=255)),
                ('text_of_hyperlink', models.TextField(blank=True)),
                ('hyperlink', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('order',),
                'db_table': 'web_trafficfine',
                'verbose_name': 'Traffic Fine',
                'verbose_name_plural': 'Traffic Fines',
            },
        ),
        migrations.CreateModel(
            name='TrafficFineCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('icon', models.FileField(upload_to=traffic_fine.models.upload_to_traffic_fine_category)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('order',),
                'db_table': 'web_trafficfinecategory',
                'verbose_name': 'Traffic Fine Category',
                'verbose_name_plural': 'Traffic Fine Categories',
            },
        ),
        migrations.CreateModel(
            name='TrafficFineCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('icon', models.FileField(upload_to=traffic_fine.models.upload_to_traffic_fine_city)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('order',),
                'db_table': 'web_trafficfinecity',
                'verbose_name': 'Traffic Fine City',
                'verbose_name_plural': 'Traffic Fine Cities',
            },
        ),
        migrations.AddField(
            model_name='trafficfine',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic_fine.TrafficFineCategory'),
        ),
        migrations.AddField(
            model_name='trafficfine',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='traffic_fine.TrafficFineCity'),
        ),
        migrations.AlterUniqueTogether(
            name='trafficfine',
            unique_together=set([('traffic_offense', 'category', 'city')]),
        ),
    ]
