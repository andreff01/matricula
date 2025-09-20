from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm


def aluno_listar(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/aluno_list.html', {'alunos': alunos})


def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm()
    return render(request, 'alunos/aluno_form.html', {'form': form})


def aluno_detalhe(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'alunos/aluno_detail.html', {'aluno': aluno})


def aluno_editar(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/aluno_form.html', {'form': form, 'aluno': aluno})


def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    return render(request, 'alunos/aluno_confirm_delete.html', {'aluno': aluno})
