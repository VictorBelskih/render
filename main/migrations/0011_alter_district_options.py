# Generated by Django 4.2.6 on 2023-11-19 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_district_alter_news_news_img_alter_slides_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': ('Район',), 'verbose_name_plural': 'Районы'},
        ),
    ]