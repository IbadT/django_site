# теперь определим все маршруты для нашего приложения
from django.urls import path
from . import views

# привязка функции вида к определенному маршруту
urlpatterns = [
    path('', views.index, name='index'), # к базовому url -> / мы привязываем функцию вида views.index
    path('<int:course_id>', views.single_course, name='single_course') # для маршрута к id
]