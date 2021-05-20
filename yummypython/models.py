# импорт пакета models для наследования от объекта Model
# import the models package to inherit from the Model object
from django.db import models
# импорт объекта Markdown для определение содержимого поля content
# import a Markdown object to define the content of the content field
from django_markdown.models import MarkdownField


# определение базы данных подтем
# define the subtopics database
class Subtopic(models.Model):
    name = models.CharField(max_length=50, default=True, verbose_name='subtopic')
    content = MarkdownField(default=True)
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, default=True)

    class Meta:
        pass

    def __str__(self):
        return self.name


# определение быза данных основных тем
# defining a database of main topics
class Topic(models.Model):
    name = models.CharField(max_length=50, default=True, db_index=True, unique=True, verbose_name='topic')

    class Meta:
        pass

    def __str__(self):
        return self.name
