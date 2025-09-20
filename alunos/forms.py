from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionar classe bootstrap aos widgets automaticamente
        for field_name, field in self.fields.items():
            css = field.widget.attrs.get('class', '')
            # selects e textarea também usam form-control
            field.widget.attrs['class'] = (css + ' form-control').strip()
