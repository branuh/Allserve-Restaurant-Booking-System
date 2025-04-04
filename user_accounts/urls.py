from django.urls import path
from todo.views import task_list
from . import views

urlpatterns = [
path('', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('home/', views.home_view, name='home'),
path('logout/', views.logout_view, name='logout'),
path('todo/', task_list, name="todoapp"),
]