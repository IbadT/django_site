# pipenv shell
# deactivate - выйти из python shell

# django-admin startproject base .
# называли base - чтобы было понятно, где находятся все настройки проекта

# python manage.py runserver
# для запуска сервера

# python manage.py startapp shop
# shop - это имя приложения

# python manage.py createsuperuser  
# для создания админа(super user)

# user -> eduard
# email -> ibadtoff@gmail.com
# password -> 12345


# python manage.py makemigrations
# для создания миграции при создании или изменеия модели бд

# python manage.py migrate
# для создания или обновления таблиц в самой бд



# работа с командной строкой

# python manage.py shell
# from shop.models import Category, Course
# для того, чтобы в самой консоли увидеть или как-то взаимодействовать с моделями
# Course.objects.all()
# <QuerySet []> - ответ в пустой таблице
# для получения всех полей из таблицы Course 

# new_category = Category(title='Programming')
# new_category.save()
# для создания и сохранения данных в бд через консоль

# new_category.title - после создания этой категории можем получить значение из поля title

# Category.objects.get(pk=1) - для получения категории по его id (pk = primary key)
# <Category: Category object (1)>

# Category.objects.get(pk=1).id 
# 1

# Category.objects.filter(title='Programming') - для фильтрации нашего запроса 
# <QuerySet [<Category: Category object(1)>]> - и после этого мы получаем его id

# category.course_set.create(title='Complete Python Guide', price=99.99, students_qty=100, review_qty=50)
# для добавления данных в таблицу Course через модель Category

# [course.title for course in Course.objects.all()] - получим список курсов из таблицы Course
# ['Complete Python Guide', 'Complete C++ Guide']





# создаем rest-api
# pip install django-tastypie

# python manage.py startapp api
# api - название папки(приложения)

# для удаления через postman необходимо указать headers
# Authorization   ApiKey eduard:_key_
# _key_ - это ключ, из admin панели
# но перед этим нужно будет добавить ключ через admin панель