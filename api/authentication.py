# в файлe api создадим файл authentication.py
# и в нем создадим кастомный класс для авторизации
from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    # в классе ApiKeyAuthentication уже есть метод is_authenticated, который отвечает за проверку(аутентифицирован пользователь или нет)
    # и в нашем собственном классе CustomAuthentication мы реализовали такой же метод, в котором мы хотим изменить поведение этого метода
    # который находится в родительском классе, но мы хотим изменить его, только если метод в запросе 'GET' и тогда мы просто пропускаем аутентификацию
    # а для всех остальных методов, мы хотим вызвать метод из родительского класса ApiKeyAuthentication метод is_authenticated
    # и для этого с помощью метода super(), временно создается экземпляр класса ApiKeyAuthentication и для него вызывается метод is_authenticated
    # которому мы передаем запрос от клиента и все именнованные аргументы
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super().is_authenticated(request, **kwargs)