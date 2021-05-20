# импорт пакета models, для определения полей базы данных приложения account
# import of the models package, to define the fields of the account application database
from django.db import models
# импорт класса AbstractUser для унаследования полей для базы данных о пользователе
# import of the AbstractUser class to inherit fields for the user database
from django.contrib.auth.models import AbstractUser


# default - значение по умолчанию, записываемое в поле, если в него явно не было занесено никакого значения
# db_index - создание индекса поля
# verbose_name - второе имя поля, которое будет отображаться на страницах веб-сайта
# upload_to - определение директории для загрузки файлов
# blank - позволяет заносить в поле пустое значение, делая поле необезательным к заполнению


# модель базы данных пользователя с унаследованием полей от модели AbstractUser
# user database model with inheritance of fields from AbstractUser model
class Profile(AbstractUser):
    # определение поля активации пользователя после регистрации
    # defining the user activation field after registration
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='activated')
    # определение поля для фотографии пользователя
    # defining the field for the user's photo
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    pixels = models.IntegerField(default=0)  # поле количества пикселей

    # унаследование настроек класса AbstractUser
    # inherit the settings of the AbstractUser class
    class Meta(AbstractUser.Meta):
        pass

    # строковое представление полей базы данных относительно username
    # string representation of database fields relative to username
    def __str__(self):
        return self.username

    # определение ссылок для задач
    # defining a link to tasks
    # def get_absolute_url(self):
    #      return '/playroom/%s/' % self.username  # <а href="{{ topic.get_absolute_url }}">{{ topic.name }}</a>
