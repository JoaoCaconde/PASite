from django.urls import path
from chamados import views

urlpatterns = [
    path('chamados/', views.ChamadosListView.as_view(), name='chamados_list'),
    path('chamados/<uuid:pk>/', views.ChamadosDetailView.as_view(), name='chamados_detail'),
    path('create-chamado/', views.CreateChamadoRPAEntradaManualView.as_view(), name='create_chamado'),
    path('update-chamado/<uuid:pk>/', views.UpdateChamadoRPAEntradaManualView.as_view(), name='update_chamado'),
    path('delete-chamado/<uuid:pk>/', views.DeleteChamadoRPAEntradaManualView.as_view(), name='delete_chamado'),
]