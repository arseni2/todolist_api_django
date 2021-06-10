from django.urls import path

from todo.views import CreateTodoS, EditTodo, addToImportantOrBin, ImportantTodo, todoDelete, todoBin, addToBin

urlpatterns = [
    path('', CreateTodoS.as_view()),
    path('important/', ImportantTodo.as_view()),
    path('edit/<int:id>', EditTodo.as_view()),
    path('add_important/', addToImportantOrBin),
    path('delete/', todoDelete),
    path('todo_bin/', todoBin),
    path('add_bin/', addToBin),
]
