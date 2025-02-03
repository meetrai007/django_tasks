from django.shortcuts import render
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from .serializers import TodosSerializer
from .models import Todos

# Create your views here.
@api_view(['GET'])
def get_todos(request,pk):
    todos = Todos.objects.filter(pk=pk)
    serializer = TodosSerializer(todos, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=TodosSerializer,
    responses={
        201: TodosSerializer,
        400: "Validation Error"
    }
)
@api_view(['POST'])
def create_todo(request):
    """
    Create a new Todo item.
    """
    serializer = TodosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method='put',
    request_body=TodosSerializer,
    responses={
        200: TodosSerializer,
        404: "Todo not found",
        400: "Validation Error"
    }
)
@api_view(['PUT'])
def update_todo(request, pk):
    """
    Update a specific Todo item by its ID.
    """
    try:
        todo = Todos.objects.get(id=pk)
    except Todos.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TodosSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = Todos.objects.get(id=pk)
    todo.delete()
    return Response('Item deleted')