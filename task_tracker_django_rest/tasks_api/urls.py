from django.urls import path
from .views import TasksApi

urlpatterns = [
    path('', view=TasksApi.as_view())
]