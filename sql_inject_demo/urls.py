from django.urls import path
from .views import sqlViewNotSecurity, sqlViewSecurity

urlpatterns = [
    path('not-security', sqlViewNotSecurity),
    path('security', sqlViewSecurity),
]