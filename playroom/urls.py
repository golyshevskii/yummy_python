# импорт метода path для обработки маршрутов
# import the path method to handle the routes
from django.urls import path
from playroom.views import *

app_name = 'playroom'

# определение маршрутов приложения playroom
# defining the routes of the playroom app
urlpatterns = [
    path('detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('<int:topic_id>/', TasksByTopic.as_view(), name='topic'),
    path('', task, name='playroom')
]