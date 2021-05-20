"""
pythonposeur URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

# импорт модуля settings + метода static для использования статических файлов во время разработки веб-сайта
# import settings module + static method to use static files during website development
from django.conf import settings
from django.conf.urls.static import static
# импорт пакета приложения admin для использования маршрутов приложения admin
# import the admin app package to use the admin app routes
from django.contrib import admin
# импорт метода path для обработки маршрутов
# import the path method to handle the routes
from django.urls import path, include


# подключение маршрутов приложений
# connecting application routers
urlpatterns = [
    path('admin/', admin.site.urls),                    # администрация сайта; administration page
    path('account/', include('account.urls')),          # приложение account; application account
    path('playroom/', include('playroom.urls')),        # приложение playroom; application playroom
    path('yummypython/', include('yummypython.urls')),  # приложение yummypython; application yummypython
    path('social-auth/', include('social_django.urls', namespace='social')),  # google авторизация; google authorization
    path('markdown/', include('django_markdown.urls')),                       # язык разметки markdown
]

# добавление(DEBUG = True) пути к сортировке статических файлов(изображения)
# add(DEBUG = True) path to sort static files(images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
