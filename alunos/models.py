from django.db import models

class Aluno(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
        ('integral', 'Integral'),
    ]
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    numero_matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20, blank=True)
    rg = models.CharField(max_length=50, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True)

    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    telefone_emergencia = models.CharField(max_length=30, blank=True)

    cep = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    numero = models.CharField(max_length=20, blank=True)
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)

    curso = models.CharField(max_length=200, blank=True)
    serie = models.CharField(max_length=100, blank=True)
    turno = models.CharField(max_length=20, choices=TURNO_CHOICES, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    observacoes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_matricula} - {self.nome}"
