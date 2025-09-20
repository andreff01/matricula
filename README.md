# Projeto Matricula

Aplicação Django simples para cadastro, listagem, edição e exclusão de alunos.

Requisitos
- Python 3.10+
- Virtualenv (recomendado)

Instalação (Windows PowerShell)

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ para ver a lista de alunos.

Se preferir, coloque o vídeo de apresentação fora do repositório e inclua um link público no README.
