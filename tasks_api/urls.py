from django.urls import path
from .views import TasksApi
from .views import TaskDetail

urlpatterns = [
    path('', view=TasksApi.as_view()),
    path('<int:id>/', view=TaskDetail.as_view())
]