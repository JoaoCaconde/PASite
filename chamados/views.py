from dj_rql.drf import RQLFilterBackend
from django.shortcuts import render
from chamados.filters import ChamadoRPAEntradaManualFilter
from rest_framework import generics
from chamados.models import ChamadoRPAEntradaManual
from chamados.serializers import ChamadoRPAEntradaManualSerializer



class ChamadosListView(generics.ListAPIView):
    """
    API view to retrieve a list of Chamados.
    """
    queryset = ChamadoRPAEntradaManual.objects.all()
    serializer_class = ChamadoRPAEntradaManualSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ChamadoRPAEntradaManualFilter
    

class ChamadosDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a specific Chamado by its primary key (pk).
    """
    queryset = ChamadoRPAEntradaManual.objects.all()
    serializer_class = ChamadoRPAEntradaManualSerializer
    
class CreateChamadoRPAEntradaManualView(generics.CreateAPIView):
    """
    API view to create a new ChamadoRPAEntradaManual.
    """
    queryset = ChamadoRPAEntradaManual.objects.all()
    serializer_class = ChamadoRPAEntradaManualSerializer
    
class UpdateChamadoRPAEntradaManualView(generics.UpdateAPIView):
    """
    API view to update an existing ChamadoRPAEntradaManual.
    """
    queryset = ChamadoRPAEntradaManual.objects.all()
    serializer_class = ChamadoRPAEntradaManualSerializer
    
class DeleteChamadoRPAEntradaManualView(generics.DestroyAPIView):
    """
    API view to delete an existing ChamadoRPAEntradaManual.
    """
    queryset = ChamadoRPAEntradaManual.objects.all()
    serializer_class = ChamadoRPAEntradaManualSerializer
    