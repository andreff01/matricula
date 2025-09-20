# Projeto Matricula

Aplicação Django simples para cadastro, listagem, edição e exclusão de alunos.

## Objetivo

Este projeto é um CRUD básico (Create / Read / Update / Delete) para alunos de uma
instituição de ensino. Foi desenvolvido para fins didáticos — foco em clareza e
funcionalidade, usando apenas Python e Django.

## Funcionalidades

- Cadastrar, listar, editar e excluir alunos
- Visualizar detalhes de cada aluno
- Painel administrativo via `/admin/` (opcional)

## Estrutura principal

- `matricula/` - configuração do projeto (settings, urls, wsgi)
- `alunos/` - app com models, views, templates e forms
- `templates/` - templates personalizados
- `static/` - CSS simples para melhorar visual
- `db.sqlite3` - banco SQLite (gerado após rodar migrations)

## Requisitos

- Python 3.10+ (recomendado)

Conteúdo de `requirements.txt`:

```
Django>=4.2
```

## Como rodar

1) Criar e ativar ambiente virtual:


python -m venv venv
venv\Scripts\Activate


2) Instalar dependências:


pip install -r requirements.txt


3) Criar e aplicar migrações (gera o banco SQLite):


python manage.py makemigrations
python manage.py migrate


4) (Opcional) Criar superuser para acessar o admin:


python manage.py createsuperuser


5) Iniciar o servidor de desenvolvimento (fica no terminal; pare com Ctrl+C):


python manage.py runserver


Abra http://127.0.0.1:8000/ no navegador para ver a lista de alunos.

## Vídeo de Apresentação

Vídeo de Apresentação na pasta `video/` arquivo `apresentacao.mp4`

Instalação

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ para ver a lista de alunos.

