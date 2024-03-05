from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    produto = models.TextField(max_length=255, default='Sem produto')
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def __str__(self):
        return self.nome