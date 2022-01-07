from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from yummypython.models import *


# отображение всех тем
def subjects(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'yummypython/yummypython.html', context)


# отображение подтем, относительно выбранной темы
class Subtopics(TemplateView):
    template_name = 'yummypython/subtopics_by_topic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtopics'] = Subtopic.objects.filter(topic=context['topic_id'])
        context['topics'] = Topic.objects.all()
        context['current_topic'] = Topic.objects.get(pk=context['topic_id'])
        return context


# отображение деталей подтемы
class SubtopicDetail(DetailView):
    model = Subtopic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        # context['current_subtopic'] = Subtopic.objects.get(pk=context['topic_id'])
        return context


# отображение страницы информации о проекте
class About(TemplateView):
    template_name = 'account/about.html'
