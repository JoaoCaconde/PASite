from django.db import models
from django.conf import settings
from costumers.models import Costumer
import uuid
from django.contrib.auth.models import User


class ChamadoRPAEntradaManual(models.Model):
    
    class Meta:
        verbose_name = 'Abertura de chamados'
        verbose_name_plural = 'Abertura de chamados'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, verbose_name='Titulo')
    xml_file = models.FileField(upload_to="xml/", verbose_name='Arquivo XML', blank=True, null=True)
    data_mov_estoque = models.DateField(verbose_name='Data de movimentação do estoque', blank=True, null=True)
    produtos_nota = models.TextField(max_length=500, verbose_name='Produtos da nota fiscal', blank=True, null=True)
    serie_nota = models.CharField(max_length=10, verbose_name='Série da nota fiscal', blank=True, null=True)
    
    
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        RETURNED = 'RETURNED', 'Retornado'
        FINISHED = 'FINISHED', 'Concluído'
        CANCELLED = 'CANCELLED', 'Cancelado'
        
        
    class typeNF(models.TextChoices):
        SP1 = 'RTE', 'RTE0753'
        SP2 = 'RME', 'RME0626'
        SP3 = 'RTE01', 'RTE0752'
           
    FRETE_CHOICES = [
        ('Sem frete', 'Sem frete'),
        ('CIF', 'CIF'),
        ('FOB', 'FOB'),
    ]
         
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        editable=True
    )
    
    message = models.TextField(max_length=500, verbose_name='Mensagem', blank=True, null=True,editable=True)
        
    key = models.CharField(max_length=44,verbose_name='Chave eletrônica da nota fiscal')
    value = models.FloatField(max_length=100,verbose_name='Valor')
    type_nf = models.CharField(
        max_length=20,
        choices=typeNF.choices,
        default=typeNF.SP1,
        verbose_name='Espécie'
    )
    frete = models.CharField(
        max_length=20,
        choices=FRETE_CHOICES,
        default='Sem frete',
    )
    cnpj_fornecedor = models.CharField(max_length=14,verbose_name='CNPJ do fornecedor', blank=True, null=True)
    cnpj_cliente = models.CharField(max_length=14,verbose_name='CNPJ do cliente', blank=True, null=True)
    cnpj_transportadora = models.CharField(max_length=14,verbose_name='CNPJ da transportadora', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, 
                                      verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, 
                                      verbose_name='Atualizado em')
    
    def __str__(self):
        return self.key


class CompletedChamadoRPAEntradaManual(ChamadoRPAEntradaManual):
    
    
    class Meta:
        proxy = True
        verbose_name = 'Chamados Concluídos'
        verbose_name_plural = 'Chamados Concluídos'