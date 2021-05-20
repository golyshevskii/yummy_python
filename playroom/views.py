# импорт метода render для формирования ответа пользователю
# import of the render method to form a response to the user
from django.shortcuts import render
# импорт декоратора login_required + LoginRequiredMixin для проверки авторизации пользователя
# import the login_required decorator + LoginRequiredMixin to check user authorization
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin
# импорт объектов для создания представления страниц
# importing objects to create page views
from playroom.models import Task, Topic
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView


# метод для отправки страницы playroom авторизованному пользователю
# method to send playroom page to authorized user
def task(request):
    tasks = Task.objects.all()
    topics = Topic.objects.all()
    # пагинатор для количества задач на одной странице
    # paginator for amount of tasks on one page
    paginator = Paginator(tasks, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'topics': topics, 'page': page, 'tasks': page.object_list}
    return render(request, 'playroom/playroom.html', context)


# класс отображения задач относительно темы
# class for displaying tasks relative to the topic
class TasksByTopic(TemplateView):
    template_name = 'playroom/tasks_by_topic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_tasks'] = Task.objects.filter(topic=context['topic_id'])
        context['topics'] = Topic.objects.all()
        context['current_topic'] = Topic.objects.get(pk=context['topic_id'])
        return context


# контроллер-класс для отображения деталей задачи
# class for displaying details of tasks
class TaskDetail(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        #context['current_topic'] = Topic.objects.get(pk=context['topic_id'])
        return context
