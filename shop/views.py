# это контроллер
# тут создаются то, что связывает видимую часть приложения с моделями
# (прием запросов от пользователя и передача ответа пользователя)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

# для прочтения наших данных из бд
# точка обязательна, тк (добавляем из текущей папки) в нашем проекте может быть много файлов с называнием model 
from .models import Course



# Create your views here.

# эту функцию назвали именно так, тк эта функция вида как раз привязана к корневой странице приложения (urls.py -> views.index)
# принимает запрос от клиента и возвращает строку
def index(request):
    courses = Course.objects.all()
    # return HttpResponse([str(course) + '<br>' for course in courses])
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))


    # 3 аргумент - это контекст вида mapping(key, value)
    return render(request, 'shop/courses.html', {'courses': courses})

# отображаем виды


def single_course(request, course_id):
    try:
        # course = Course.objects.get(pk=course_id)
        course = get_object_or_404(Course, pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    except Course.DoesNotExist:
        raise Http404()