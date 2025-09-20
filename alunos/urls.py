from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlunoListView.as_view(), name='aluno_list'),
    path('novo/', views.AlunoCreateView.as_view(), name='aluno_create'),
    path('<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno_update'),
    path('<int:pk>/excluir/', views.AlunoDeleteView.as_view(), name='aluno_delete'),
]
