from django.contrib import admin
from django.urls import path, include
from gerenciar import views  # Importa as views do app 'gerenciar'

urlpatterns = [
    path('login/', views.login_paciente, name='login_paciente'),  # A URL para /login/
    path('admin/', admin.site.urls),  # A URL para o painel de administração
    path('gerenciar/', include('gerenciar.urls')),  # Inclui as URLs do app 'gerenciar'
    path('', views.login_paciente, name='login'),  # Corrigido o nome da URL para 'login'
]


