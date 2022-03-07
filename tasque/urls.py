from django.urls import path
from . import views

app_name = 'tasque'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/create/complete/', views.TaskCreateCompleteView.as_view(),
         name='task_create_complete'),
    path('task/do/<int:tag_id>/', views.taskDoView, name='task_do'),
    path('task/delete/<uuid:task_id>',
         views.taskDeleteView, name='task_delete'),
    path('task/done/<uuid:task_id>', views.taskDoneView, name='task_done'),
]
