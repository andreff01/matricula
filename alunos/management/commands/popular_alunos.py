from django.core.management.base import BaseCommand
from alunos.models import Aluno
import random

NOMES = [
    'Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
    'Lucas', 'Mariana', 'Nicolas', 'Olivia', 'Paulo', 'Quésia', 'Rafael', 'Sofia', 'Tiago', 'Vitória'
]
SOBRENOMES = [
    'Silva', 'Souza', 'Oliveira', 'Santos', 'Pereira', 'Lima', 'Carvalho', 'Ferreira', 'Almeida', 'Costa',
    'Martins', 'Rocha', 'Barbosa', 'Ramos', 'Teixeira', 'Gomes', 'Mendes', 'Araujo', 'Moura', 'Batista'
]

def gerar_nome():
    return f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}"

def gerar_matricula():
    return str(random.randint(20221094010000, 20221094999999))

class Command(BaseCommand):
    help = 'Popula o banco com 100 alunos de teste.'

    def handle(self, *args, **kwargs):
        # Remove todos os alunos antes de popular
        Aluno.objects.all().delete()
        criados = 0
        for i in range(1, 101):
            nome = gerar_nome()
            matricula = gerar_matricula()
            Aluno.objects.create(
                numero_matricula=matricula,
                nome=nome,
                cpf=f"000.000.000-{i:02d}",
                rg=f"MG-{i:05d}",
                data_nascimento="2000-01-01",
                sexo=random.choice(['M', 'F', 'O']),
                email=f"{nome.lower().replace(' ','.')}@teste.com",
                telefone="(31) 99999-0000",
                telefone_emergencia="(31) 98888-0000",
                cep="30000-000",
                endereco="Rua Exemplo",
                numero="123",
                complemento="Apto 1",
                bairro="Centro",
                cidade="Cidade Teste",
                uf="MG",
                curso="Curso Teste",
                serie="1º",
                turno=random.choice(['manha','tarde','noite','integral']),
                status="ativo" if i % 2 == 0 else "inativo",
                observacoes="Aluno gerado automaticamente."
            )
            criados += 1
        self.stdout.write(self.style.SUCCESS(f'{criados} alunos criados com sucesso!'))
