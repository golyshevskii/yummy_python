from django.contrib import admin
from yummypython.models import *


class SubtopicView(admin.ModelAdmin):
    list_display = ['name', 'topic']
    list_display_links = ['name']
    search_fields = ['name', 'topic']


admin.register(Subtopic, SubtopicView)


class TopicView(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.register(Topic, TopicView)
