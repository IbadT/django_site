# сюда следует добавлять настройки административной части для конкретного приложения
# для того, чтобы зарегистрировать наши модели, для работы с ними в админ панели
from django.contrib import admin


# Register your models here.


from . import models

# для изменения параметров в панели администратора
admin.site.site_header = 'Courses Admin'
admin.site.site_title = 'My App'
admin.site.index_title = "Welcome to the Courses admin area"

# с помощью этого класса мы добавим таблицу с курсами на странице категории
class CoursesInline(admin.TabularInline):
    model = models.Course
    exclude = ['created_at']
    extra = 1 # сколько доп рядов доступно для создания новых курсов


# без этого класса будет только title в панели администратора
class CourseAdmin(admin.ModelAdmin):
    # с помощью этого атрибута можно указать, какие поля будут отображаться в веб интерфейсе администратора для определенной модели
    list_display = ('title', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'], 
            'classes': ['collapse']
            }
        )
    ]
    inlines = [CoursesInline]


# регистрируем две наши модели
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)