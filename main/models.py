from django.db import models
from ckeditor.fields import RichTextField

import os
class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_img = models.ImageField(upload_to='image/')
    news_text = models.TextField()
    news_date = models.DateTimeField("date published")

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость',
        verbose_name_plural = 'Новости'

class Slides(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='image/')
    text = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайды',
        verbose_name_plural = 'Слайды'

class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey('Articles_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья',
        verbose_name_plural = 'Статьи'

class Articles_category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория',
        verbose_name_plural = 'Категории'

class District(models.Model):
    districtCode = models.IntegerField(50)
    districtName = models.CharField(200)

    def __str__(self):
        return self.districtName








