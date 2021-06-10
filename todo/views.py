from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import TodoListModel
from todo.serializers import TodoListSerializer

class CreateTodoS(generics.ListCreateAPIView):
    queryset = TodoListModel.objects.all()
    serializer_class = TodoListSerializer

class ImportantTodo(generics.ListAPIView):
    queryset = TodoListModel.objects.filter(is_importants=True)
    serializer_class = TodoListSerializer

class EditTodo(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = TodoListModel.objects.all()
    serializer_class = TodoListSerializer

@api_view(['POST', ])
def addToImportantOrBin(request):
    todo_id = request.POST.get('todo_id')
    current_todo = TodoListModel.objects.get(id=todo_id)
    current_todo.is_importants = True
    current_todo.save()
    s = TodoListSerializer(current_todo).data
    return Response(s)
@api_view(['POST', ])
def addToBin(request):
    todo_id = request.POST.get('todo_id')
    current_todo = TodoListModel.objects.get(id=todo_id)
    current_todo.is_delete = True
    current_todo.save()
    todos = TodoListModel.objects.filter(is_delete=True)
    s = TodoListSerializer(todos, many=True).data
    return Response(s)    
@api_view(['POST', ])
def todoDelete(request):
    todo_id = request.POST.get('todo_id')
    current_todo = TodoListModel.objects.filter(id=todo_id).delete()
    todos = TodoListModel.objects.filter(is_delete=True)
    s = TodoListSerializer(todos, many=True).data
    return Response(s)

@api_view(['GET', ])
def todoBin(request):
    todo = TodoListModel.objects.filter(is_delete=True)
    s = TodoListSerializer(todo, many=True).data
    return Response(s)

