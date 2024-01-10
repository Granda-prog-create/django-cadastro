from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuarios/usuarios.html', usuarios)

def deletar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('listagem_usuarios')  # Redirecionar para a página de usuários após a exclusão
    
    return render(request, 'usuarios/deletar_usuario.html', {'usuario': usuario})
