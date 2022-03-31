from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
]
