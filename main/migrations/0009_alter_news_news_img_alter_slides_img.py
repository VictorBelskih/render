# Generated by Django 4.2.6 on 2023-10-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_pageelement_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_img',
            field=models.ImageField(upload_to='media/static/AgroChemical/image/'),
        ),
        migrations.AlterField(
            model_name='slides',
            name='img',
            field=models.ImageField(upload_to='media/static/AgroChemical/image/'),
        ),
    ]
