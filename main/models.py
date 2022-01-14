from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок новости')
    content = models.TextField(max_length=2000, verbose_name='содержание статьи')
    image = models.ImageField(verbose_name='изображение статьи')
    published = models.DateField(auto_now=True)
    type = models.CharField(max_length=20, verbose_name='тип новостей')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
