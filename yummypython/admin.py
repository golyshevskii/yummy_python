from django.db import models
from django.contrib import admin
from yummypython.models import Subtopic, Topic
from martor.widgets import AdminMartorWidget


class SubtopicView(admin.ModelAdmin):
    list_display = ['name', 'topic']
    list_display_links = ['name']
    search_fields = ['name', 'topic']
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }


# admin.site.register(Subtopic, SubtopicView)
admin.site.register(Subtopic, SubtopicView)


class TopicView(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Topic, TopicView)
