from django import forms
from .models import Obra

class ObraForm(form.ModelForm):
    class Meta:
        model:Obra
        fields: ["titulo", "tipo", "ano" "genero", "descricao"]
        
