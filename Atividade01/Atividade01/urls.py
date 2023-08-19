from django.contrib import admin
from django.urls import path
from App_Atividade01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('home/', views.home, name='home'),
    path('obter_usuario/', views.obter_usuario, name='obter_usuario'),
    path('usuario_criado/', views.usuario_criado, name='usuario_criado'),  # Nova URL para a página de confirmação
]
