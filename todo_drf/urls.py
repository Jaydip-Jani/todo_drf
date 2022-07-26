'''
# Generic APIView and Model Mixin

from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('todoapi_1/', views.TodoList.as_view()),
    path('todoapi_2/<int:pk>/', views.TodoDetail.as_view()),


    path('todoapi_1/', views.TodoList.as_view()),
    path('todoapi_1/', views.TodoCreate.as_view()),
    path('todoapi_1/<int:pk>/', views.TodoRetrive.as_view()),
    path('todoapi_1/<int:pk>/', views.TodoUpdate.as_view()),
    path('todoapi_1/<int:pk>/', views.TodoDelete.as_view()),
]
'''

from django.contrib import admin
from django.urls import path, include
from todoapp import views
from rest_framework.routers import DefaultRouter

# Creating Router

router = DefaultRouter()

# Register TodoViewSet with Router

router.register('todoapi', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
