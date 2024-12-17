from django.shortcuts import render
from cadastrar.views import Produto
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.

def exc_produto(request):
    produtos = Produto.objects.all()
    if request.method =="GET":
        return render(request, 'excluir.html', {'produtos': produtos})
    elif request.method =="POST":
        produto_id = request.POST.get('nome_produto')

        exc_nome = Produto.objects.get(id=produto_id)
        exc_nome.delete()
        
        messages.add_message(request, constants.SUCCESS, 'Exclusão Realizada')
        return render(request, 'excluir.html', {'produtos': produtos})

