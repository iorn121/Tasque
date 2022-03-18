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
    path('tag/list/', views.TagListView, name='tag_list'),
    path('tag/create/', views.tagCreateView, name='tag_create'),
    path('tag/delete/<int:tag_id>/', views.tagDeleteView, name='tag_delete'),
    path('tag/create/complete/', views.TagCreateCompleteView.as_view(),
         name='tag_create_complete'),
]
