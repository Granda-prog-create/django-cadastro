from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    produto = models.TextField(max_length=255, default='Sem produto')

    def __str__(self):
        return self.nome