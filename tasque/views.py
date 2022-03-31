from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView
from .forms import TaskForm, TagForm
from django.db.models import F
from .models import Task, TaskTag
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone


class IndexView(TemplateView):
    template_name = 'index.html'


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super().form_valid(form)
    success_url = reverse_lazy('tasque:task_create_complete')


def TagListView(request):
    template_name = 'tag_list.html'
    tag_list = {}
    qs = TaskTag.objects.all()
    tag_list['tag_list'] = qs
    return render(request, template_name, tag_list)


class TaskCreateCompleteView(TemplateView):
    template_name = 'task_create_complete.html'


# class TagCreateCompleteView(TemplateView):
#     template_name = 'tag_create_complete.html'


def taskDoView(request, tag_id):
    template_name = 'task_do.html'
    todolist = {}
    tg = TaskTag.objects.get(id=tag_id)
    all_tag = TaskTag.objects.all()
    qs = Task.objects.filter(tag=tg, status=0).order_by(
        F('due_date').asc(nulls_last=True))
    todolist['all_tag'] = all_tag
    todolist['now_tag'] = tg
    todolist['tasks'] = qs
    return render(request, template_name, todolist)


@require_POST
def tagCreateView(request):
    tag_name = request.POST['tag_name']
    if tag_name:
        TaskTag.objects.create(name=tag_name)
    return redirect('tasque:tag_list')


@require_POST
def tagDeleteView(request, tag_id):
    tag = get_object_or_404(TaskTag, id=tag_id)
    if tag:
        tag.delete()
    return redirect('tasque:tag_list')


@require_POST
def taskDeleteView(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task:
        task.delete()
    return redirect('tasque:task_do', task.tag.id)


@require_POST
def taskDoneView(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task:
        task.status = 1
        task.finished_at = timezone.now()
        task.save()
    return redirect('tasque:task_do', task.tag.id)
