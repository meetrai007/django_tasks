from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodosSerializer
from .models import Todos

# Create your views here.
@api_view(['GET'])
def get_todos(request):
    todos = Todos.objects.all()
    serializer = TodosSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo(request):
    serializer = TodosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_todo(request, pk):
    todo = Todos.objects.get(id=pk)
    serializer = TodosSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = Todos.objects.get(id=pk)
    todo.delete()
    return Response('Item deleted')