from django.db import models

# Create your models here.

# после добавления класса CustomAuthentication добавим импорты
# класс, который отвечает за авторизацию пользователей
from tastypie.authorization import Authorization

from .authentication import CustomAuthentication

# модели в терминах api - называются ресурсами
from tastypie.resources import ModelResource
from shop.models import Category, Course

class CategoryResource(ModelResource):
    # Meta - это собственный атрибут класса CategoryResource
    class Meta:
        queryset = Category.objects.all()
        # имя, которое мы будем указывать в пути при получения доступа к api сервиса
        resource_name = 'categories'
        # разрешаем только get метод в rest-api сервисе, остальные методы будут запрещены
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['created_at'] # для того, чтобы исключить поле created_at из списка, отправленному для пользователя

        # добавим атрибуты для добавления авторизации и аутентификации
        authentication = CustomAuthentication()
        authorization = Authorization()

        # добавим 2 метода для того, чтобы можно было напрямую указывать category_id, тк по умолчанию - это запрещено в django
        # функция hydrate позволяет нам вставить в объект category_id и мы возьмем его из bundle
        def hydrate(self, bundle):
            # bundle - данные, которые приходят от клиента
            # при отправке 'POST' запроса, мы из данных, которые приходят от клиента возьмем category_id и добавим объекту course - category_id
            bundle.obj.category_id = bundle.data['category_id']
            return bundle
        
        # в этой функции мы выполним обратную операцию (этот метод добавляет поле category_id в наши данные, которые мы получаем в 'GET')
        def dehydrate(self, bundle):
            bundle.data['category_id'] = bundle.obj.category_id 
            return bundle
        
        # добавим метод для изменения данных, перед отправкой пользователю
        def dehydrate_title(self, bundle):
            return bundle.data['title'].upper() # и теперь все заголовки возвращаются клиенту в верхнем регистре


# для установки лимита (по default limit=20)
# 127.0.0.1:8000/api/courses/?limit=10 