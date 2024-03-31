from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('mark-as-completed/<int:item_id>/', views.mark_as_completed, name="mark_as_completed"),
    path('remove/<int:item_id>/', views.remove_todo, name="remove_todo"),
]
