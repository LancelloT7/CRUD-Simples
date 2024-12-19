from django.urls import path
from . import views

urlpatterns = [
    path('exc_produto/', views.exc_produto, name='exc_produto'),
]
