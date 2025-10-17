from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm


def aluno_listar(request):
    # Filtros
    nome = request.GET.get('nome', '').strip()
    status = request.GET.get('status', '').strip()
    alunos = Aluno.objects.all()
    if nome:
        alunos = alunos.filter(nome__icontains=nome)
    if status:
        alunos = alunos.filter(status=status)

    # Paginação
    from django.core.paginator import Paginator
    paginator = Paginator(alunos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Info de paginação
    total = paginator.count
    start = (page_obj.number - 1) * paginator.per_page + 1 if total > 0 else 0
    end = start + len(page_obj.object_list) - 1 if total > 0 else 0

    context = {
        'alunos': page_obj.object_list,
        'page_obj': page_obj,
        'paginator': paginator,
        'total': total,
        'start': start,
        'end': end,
        'nome': nome,
        'status': status,
    }
    return render(request, 'alunos/aluno_list.html', context)


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
