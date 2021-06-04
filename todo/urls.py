from django.urls import path

from todo.views import CreateTodo, EditTodo, addToImportantOrBin, ImportantTodo, toComplete, todoBin

urlpatterns = [
    path('', CreateTodo.as_view()),
    path('important/', ImportantTodo.as_view()),
    path('edit/<int:id>', EditTodo.as_view()),
    path('add_important/', addToImportantOrBin),
    path('add_complete/', toComplete),
    path('todo_bin/', todoBin),
]
