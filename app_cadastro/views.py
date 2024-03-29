from django.shortcuts import render, redirect
from .models import Usuario
from decimal import Decimal

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.produto = request.POST.get('produto')

        # Converter o valor para Decimal antes de salvar
        valor = request.POST.get('valor').replace(',', '.')  # Substituir vírgula por ponto
        novo_usuario.valor = Decimal(valor)
        novo_usuario.save()
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

def deletar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id_usuario=usuario_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('listagem_usuarios')  # Redireciona após a exclusão

    return render(request, 'usuarios/deletar_usuario.html', {'usuario': usuario})

def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id_usuario=usuario_id)

    if request.method == 'POST':
        usuario.produto = request.POST.get('produto')
        usuario.valor = request.POST.get('valor')  # Atualiza o valor do produto
        usuario.save()
        return redirect('listagem_usuarios')  # Redireciona após a edição

    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})