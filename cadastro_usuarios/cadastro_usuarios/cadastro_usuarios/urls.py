from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsável e nome de referência. 
    path('',views.home,name='home'), 
    path('usuarios/',views.usuarios,name='listagem_usuarios'), 
    path('deletar_usuario/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),

]