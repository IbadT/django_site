"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include




# импортируем модели наших классов из api
from api.models import CourseResource, CategoryResource

from tastypie.api import Api

# создаем экземпляры наших классов
course_resource = CourseResource()
category_resource = CategoryResource()


# для нашего api зарегистрируем наши ресурсы
api = Api(api_name='v1') # версия api
# регистрируем их для нашего api
api.register(course_resource)
api.register(category_resource)
# до этого было
# api/courses/
# api/categories/

# теперь наши пути будут выглядеть так
# api/v1/courses/
# api/v1/categories/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')), # включаем все маршруты, которые мы описали в файле shop/urls.py (главная страница)

    # после регистрации нашего api, нужно удалить 1 из наших путей и изменим его
    # path('api/', include(course_resource.urls)),
    # path('api/', include(category_resource.urls))

    # подключаем все ресурсы этого api, по пути api
    path('api/', include(api.urls))
]
