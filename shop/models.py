# тут создаются модели для базы данных

from django.db import models
from django.utils import timezone

# Create your models here.



# models.Model - является родительским классом для наших классов

class Category(models.Model):
    title = models.CharField(max_length=255) # значение будет в виде строки
    created_at = models.DateTimeField(default=timezone.now) # чтобы значение создавалось автоматически и указывалась текущая дата
    
    # для отображения имени нашей модели в админ панели
    # до этого было Course object (2) -> стало Programming
    # этот магический метод указывает на то, как конвертировать объект определенного класса в строку
    def __str__(self) -> str:
        return self.title 


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # one_delete=models.CASCADE - означает, что при удалении определенной категории, автоматически будут удалены ВСЕ курсы в этой категории
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

# для того, чтобы эти таблицы появились, нам нужно создать миграции для нашего приложения shop и применить эти миграции
# python manage.py makemigrations - эта команда создаст необходимые миграции для ВСЕХ приложений, которые зарегистрированы в нашем проекте