from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login

def login_paciente(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']
            user = authenticate(request, username=cpf, password=senha)
            if user is not None:
                login(request, user)
                return redirect('dashboard_paciente')  
            else:
                form.add_error(None, 'Credenciais inválidas')
    else:
        form = LoginForm()
    return render(request, 'gerenciar/login.html', {'form': form})  # Aqui, corrigimos o caminho
