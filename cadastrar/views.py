from django.shortcuts import render
from .models import Produto
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.


def cad_produto(request):
    produtos = Produto.objects.all()
    if request.method =="GET":
        return render(request, 'cadastrar.html', {'produtos': produtos})
    elif request.method =="POST":
        nome = request.POST.get('nome_produto')
        try:
            produto = Produto(nome=nome)
            produto.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro Realizado')
            return render(request, 'cadastrar.html', {'produtos': produtos})
        except:
            messages.add_message(request, constants.ERROR, 'Não foi possivel realizar o cadastro')
            return render(request, 'cadastrar.html', {'produtos': produtos})


