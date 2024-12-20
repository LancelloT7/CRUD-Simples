from django.shortcuts import render, redirect
from produtos.views import Produto
from django.contrib import messages
from django.contrib.messages import constants
from PIL import Image

# Create your views here.


def cad_produto(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        return render(request, 'cadastrar.html', {'produtos': produtos})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome_produto')
        file = request.FILES.get('my_file')

        if not nome or not file:
            messages.add_message(
                request, constants.ERROR, 'Nome e imagem são obrigatórios.'
            )
            return redirect('cad_produto')

        try:
            produto = Produto(nome=nome, img=file)
            produto.save()

            messages.add_message(
                request, constants.SUCCESS, 'Cadastro realizado com sucesso!'
            )
            return redirect('cad_produto')
        except Exception as e:
            messages.add_message(
                request, constants.ERROR, f'Erro ao cadastrar o produto: {str(e)}'
            )
            return redirect('cad_produto')
