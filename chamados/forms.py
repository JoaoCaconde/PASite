from django import forms
from chamados.models import ChamadoRPAEntradaManual


class ChamadoRPAEntradaManualForm(forms.ModelForm):
    
    class Meta:
        model = ChamadoRPAEntradaManual
        fields = "__all__"
        
        
    def clean(self):
        frete = self.cleaned_data.get('frete')
        key = self.cleaned_data.get('key')
        xml_file = self.cleaned_data.get('xml_file')
        cnpj_fornecedor = self.cleaned_data.get('cnpj_fornecedor')
        cnpj_cliente = self.cleaned_data.get('cnpj_cliente')
        cnpj_transportadora = self.cleaned_data.get('cnpj_transportadora')
        created_at = self.cleaned_data.get('created_at')
        if created_at != None or str(key) == "None":
           raise forms.ValidationError(' Não pode ser enviado.') 
        
        if len(key) < 44:
            raise forms.ValidationError(' O campo key não pode ter menos de 44 caracteres.')
        
        elif len(key) > 44:
            raise forms.ValidationError(' O campo key não pode ter mais de 44 caracteres.')
        
        if frete != 'Sem frete':
            if not cnpj_fornecedor or not cnpj_cliente or not cnpj_transportadora:
                raise forms.ValidationError(' Os campos CNPJ do fornecedor, CNPJ do cliente e CNPJ da transportadora são obrigatórios quando o frete não é "Sem frete".')
        
        return self.cleaned_data
