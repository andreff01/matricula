from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('numero_matricula', 'nome', 'cpf', 'curso', 'serie', 'turno', 'status')
    search_fields = ('numero_matricula', 'nome', 'cpf')
