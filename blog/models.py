from django.conf import settings
from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField("Название", max_length=200)
    post = models.TextField("Пост")
    image = models.ImageField("Изображение", upload_to='images',)
    blog_date = models.DateField("Дата публикации", default=timezone.now)
    draft = models.BooleanField('Статус', default=0)


    def publish(self):
        self.blog_date = timezone.now()
        self.save()

    def __str__(self):
        return f' "{self.title}"'+f' от {self.blog_date}'



class Comment(models.Model):
    author = models.CharField("Название", max_length=200)
    email = models.EmailField("E-mail")
    text = models.TextField("Комментарий",)
    date = models.DateTimeField("Дата публикации", default=timezone.now)
    status = models.BooleanField('Статус', default=0)


    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return f' "{self.author}"'+f' от {self.date}'




