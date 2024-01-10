from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('usuarios/', views.usuarios, name='listagem_usuarios'), 
    path('deletar_usuario/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),  
]
