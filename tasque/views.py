from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView
from .forms import TaskForm
from django.db.models import F
from .models import Task, TaskTag
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST


class IndexView(TemplateView):
    template_name = 'index.html'


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasque:task_create_complete')


class TaskCreateCompleteView(TemplateView):
    template_name = 'task_create_complete.html'


def taskDoView(request, tag_id):
    template_name = 'task_do.html'
    todolist = {}
    tg = TaskTag.objects.get(id=tag_id)
    all_tag = TaskTag.objects.all()
    qs = Task.objects.filter(tag=tg, status=0).order_by(
        F('due_date').asc(nulls_last=True))
    todolist['all_tag'] = all_tag
    todolist['tasks'] = qs
    return render(request, template_name, todolist)


@require_POST
def taskDeleteView(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task:
        task.delete()
    return redirect('tasque:task_do', task.tag.id)
