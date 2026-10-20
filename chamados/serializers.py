from rest_framework import serializers
from chamados.models import ChamadoRPAEntradaManual


class ChamadoRPAEntradaManualSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = ChamadoRPAEntradaManual
        fields = '__all__'