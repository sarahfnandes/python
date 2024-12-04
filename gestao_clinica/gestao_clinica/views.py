
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from gerenciar.forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_paciente(request):
    paciente = request.user.paciente  
    return render(request, 'dashboard_paciente.html', {'paciente': paciente})

def login_paciente(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']
            
        
            user = authenticate(request, username=cpf, password=senha)
            if user is not None:
                login(request, user)
                return redirect('paciente_dashboard') 
            else:
                form.add_error(None, "CPF ou senha inválidos")
    else:
        form = LoginForm()

    return render(request, 'gerenciar/login.html', {'form': form})

