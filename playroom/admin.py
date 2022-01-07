# импорт моделей баз данных и пакета admin для регистрации и формирования представления полей модели
# import of database models and the admin package to register and form the representation of the model fields
from django.db import models
from django.contrib import admin
from playroom.models import Task, Topic, Difficulty, Pixel
from martor.widgets import AdminMartorWidget


# list_display - атрибут, задает набор выводимых в списке полей
# search_fields - атрибут, указывает перечень полей модели, по которым будет выполняться фильтрация записей
# list_display_links - атрибут, задает ссылку на поле


class TaskView(admin.ModelAdmin):
    list_display = ['title', 'topic', 'difficulty', 'pixels', 'author']
    list_display_links = ['title']
    search_fields = ['title', 'topic', 'difficulty', 'pixels', 'author']
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }


admin.site.register(Task, TaskView)


class TopicView(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Topic, TopicView)


class DifficultyView(admin.ModelAdmin):
    list_display = ['name', 'pixels']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Difficulty, DifficultyView)


class PixelView(admin.ModelAdmin):
    list_display = ['score']
    list_display_links = ['score']
    search_fields = ['score']


admin.site.register(Pixel, PixelView)
