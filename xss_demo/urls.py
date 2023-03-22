from django.urls import path
from .views import not_security_view, security_view

urlpatterns = [
    path('not-security', not_security_view, name='xss-not-security'),
    path('security', security_view, name='xss-security'),
]