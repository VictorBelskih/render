# Generated by Django 4.2.6 on 2023-11-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_farm'),
    ]

    operations = [
        migrations.CreateModel(
            name='TLU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': ('Тип поля',),
                'verbose_name_plural': 'Тип полей',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField()),
                ('area', models.FloatField()),
                ('GEOM', models.TextField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.farm')),
                ('tlu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tlu')),
            ],
            options={
                'verbose_name': ('Поля',),
                'verbose_name_plural': 'Поля',
            },
        ),
    ]
