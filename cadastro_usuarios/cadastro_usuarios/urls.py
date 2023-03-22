from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsável e nome de referência. 
    path('',views.home,name='home'), 
    path('usuarios/',views.usuarios,name='listagem_usuarios'), 
]
