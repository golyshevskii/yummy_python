# импорт пакета models, для определения полей базы данных приложения playroom
# import of the models package, to define the fields of the playroom application database
from django.db import models
# импорт модели базы данных пользователя для установления связи между моделями
# import a user database model to establish a relationship between models
from account.models import Profile


# default - присваивает полю значение по умолчанию, если поле явно не определено
# on_delete - предотвращение удаления записи первичной модели, при удалении записи во вторичной модели
# unique — если True, то в текущее поле может быть занесено только уникальное в пределах таблицы значение
# db_index - создание индекса поля


# модель базы данных задач
# database model of tasks
class Task(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, null=True)  # поле темы
    title = models.CharField(max_length=50, default=True)  # поле названия задачи
    content = models.TextField(default=True)               # поле описания задачи
    difficulty = models.ForeignKey('Difficulty', on_delete=models.PROTECT, null=True)  # поле сложности задачи
    pixels = models.ForeignKey('Pixel', on_delete=models.PROTECT, null=True)  # поле количества балов задачи
    author = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)   # поле автора задачи

    # настройки модели
    # model settings
    class Meta:
        ordering = ['topic', 'difficulty']

    # строковое представление полей модели
    # string representation of model fields
    def __str__(self):
        return self.title

    # определение ссылки для автора задачи
    # defining a link for the author task
    # def get_absolute_url(self):
    #     return '/account/%s/' % self.author  # <а href="{{ tasks.get_absolute_url }}">{{ tasks.author }}</a>


# модель базы данных тем
# database model of topics
class Topic(models.Model):
    name = models.CharField(max_length=50, default=True, db_index=True, unique=True, verbose_name='topic')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # определение ссылки для фильтрации задач относительно тем
    # defining a link to filter tasks relative to topics
    # def get_absolute_url(self):
    #     return '/playroom/%s/' % self.name  # <а href="{{ topic.get_absolute_url }}">{{ topic.name }}</a>


# модель базы данных сложности задачи
# database model of task difficulty
class Difficulty(models.Model):
    name = models.CharField(max_length=50, default=True, verbose_name='difficulty')
    pixels = models.OneToOneField('Pixel', on_delete=models.PROTECT)

    class Meta:
        pass

    def __str__(self):
        return self.name


# модель базы данных балов задачи
# database model of task score
class Pixel(models.Model):
    score = models.IntegerField(default=5, verbose_name='pixels')

    class Meta:
        pass

    def __str__(self):
        return str(self.score)
