from django.urls import path
from . import views

urlpatterns = [
    path('edt_produto/', views.edt_produto, name='edt_produto'),
]
