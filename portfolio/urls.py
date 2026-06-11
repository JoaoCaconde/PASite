from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sobreMim/', views.sobreMim, name='sobreMim'),
    path('contato/', views.contato, name='contato'),
    path('habilidades/', views.habilidades, name='habilidades'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]