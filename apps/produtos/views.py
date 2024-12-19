from django.shortcuts import render
from .models import Produto

# Create your views here.


def listar(request):
    produtos = Produto.objects.all()
    return render(request, 'listar.html', {'produtos': produtos})
