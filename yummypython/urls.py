from django.urls import path
from yummypython.views import *


app_name = 'yummypython'


urlpatterns = [
    path('detail/<int:pk>/', SubtopicDetail.as_view(), name='subtopic_detail'),
    path('<int:topic_id>/', Subtopics.as_view(), name='subtopics_by_topic'),
    path('', subjects, name='yummypython')
]