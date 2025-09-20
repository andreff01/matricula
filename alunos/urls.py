from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno_listar, name='aluno_list'),
    path('novo/', views.aluno_criar, name='aluno_create'),
    path('<int:id>/', views.aluno_detalhe, name='aluno_detail'),
    path('<int:id>/editar/', views.aluno_editar, name='aluno_update'),
    path('<int:id>/excluir/', views.aluno_remover, name='aluno_delete'),
]
