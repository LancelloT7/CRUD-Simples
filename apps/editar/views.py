from django.shortcuts import render, redirect
from produtos.views import Produto
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.


def edt_produto(request):
    produtos = Produto.objects.all()
    if request.method == 'GET':
        return render(request, 'editar.html', {'produtos': produtos})
    elif request.method == 'POST':
        produto_id = request.POST.get('nome_produto')
        novo_nome = request.POST.get('novo_nome')

        produto = Produto.objects.get(id=produto_id)
        produto.nome = novo_nome
        produto.save()

        messages.add_message(
            request, constants.SUCCESS, 'Atualização Realizada'
        )
        return redirect('edt_produto')
