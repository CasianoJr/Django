from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_view, name='todo_view'),
    path('add/', views.todo_add, name='todo_add'),
    path('delete/all/', views.todo_delete_all, name='todo_delete_all'),
    path('delete/completed/', views.todo_delete_completed,
         name='todo_delete_completed'),
    path('completed/<pk>/', views.todo_mark_completed, name='todo_mark_completed'),
    path('incomplete/<pk>/', views.todo_mark_incomplete,
         name='todo_mark_incomplete'),
    path('delete/<pk>/', views.todo_delete, name='todo_delete'),

]
