from django.urls import path
from .views import api_view

urlpatterns = [
    path('', view=api_view)
]