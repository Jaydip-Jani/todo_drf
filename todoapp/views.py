'''
# Generic APIView and Model Mixin

from rest_framework import generics
from rest_framework import mixins
from .serializers import *
from .models import *


class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class TodoList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TodoCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodoRetrive(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TodoUpdate(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class TodoDelete(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ViewSet Class

from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *


class TodoViewSet(viewsets.ViewSet):
    def list(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def retrive(self, request, pk=None):
        id = pk
        if id is not None:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializers.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        todo = Todo.objects.get(pk=id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        todo = Todo.objects.get(pk=id)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def destrory(self, request, pk):
        id = pk
        todo = Todo.objects.get(pk=id)
        todo.delete()
        return Response({'msg': 'Data Deleted'})
'''

# ModelViewSet

from .models import *
from .serializers import *
from rest_framework import viewsets


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

'''

# ReadOnlyModelViewSet

from .models import *
from .serializers import *
from rest_framework import viewsets


class TodoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
'''
