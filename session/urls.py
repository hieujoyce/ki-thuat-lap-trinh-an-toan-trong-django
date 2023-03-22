from django.urls import path
from .views import session_view

urlpatterns = [
    path('', session_view, name='session'),
]