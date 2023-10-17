from django import forms
from django.contrib import admin
from .models import News, Slides, Articles, Articles_category
from ckeditor.widgets import CKEditorWidget
# Register your models here.

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticlesAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Articles
        fields = '__all__'
class NewsAdminForm(forms.ModelForm):
    news_text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'
class ArticlesAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

admin.site.register(News,NewsAdmin)
admin.site.register(Slides)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Articles_category)





