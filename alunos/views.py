from django.urls import reverse_lazy
from django.views import generic
from .models import Aluno
from .forms import AlunoForm

class AlunoListView(generic.ListView):
    model = Aluno
    template_name = 'alunos/aluno_list.html'
    context_object_name = 'alunos'


class AlunoCreateView(generic.CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/aluno_form.html'
    success_url = reverse_lazy('aluno_list')


class AlunoDetailView(generic.DetailView):
    model = Aluno
    template_name = 'alunos/aluno_detail.html'
    context_object_name = 'aluno'


class AlunoUpdateView(generic.UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/aluno_form.html'
    success_url = reverse_lazy('aluno_list')


class AlunoDeleteView(generic.DeleteView):
    model = Aluno
    template_name = 'alunos/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno_list')
