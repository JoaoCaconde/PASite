from django.db import models
from django.contrib.auth.models import User


class Costumer(models.Model):
    user = models.OneToOneField(
         User,
         null=True,
         blank=True,
         related_name='costumer',
         verbose_name='Usuário',
         on_delete=models.PROTECT)

    name = models.CharField(max_length=100,verbose_name='Nome')
    cpf = models.CharField(max_length=15,
                           verbose_name='CPF',
                           blank=True,
                           null=True)
    phone = models.CharField(max_length=15,
                             verbose_name='Telefone',
                             blank=True,
                             null=True)
    created_at = models.DateTimeField(auto_now_add=True, 
                                      verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, 
                                      verbose_name='Atualizado em')
    
    class Meta:
        verbose_name = 'Cadastro de cliente'
        verbose_name_plural = 'Cadastro de clientes'
        
    def __str__(self):
        return self.name