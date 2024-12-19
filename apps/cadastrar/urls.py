from django.urls import path
from . import views


urlpatterns = [

    path('cad_produto/', views.cad_produto, name='cad_produto'),
]