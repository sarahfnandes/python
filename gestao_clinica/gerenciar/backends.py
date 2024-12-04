from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from gerenciar.models import Paciente

class CPFBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if not username or not password:
            return None
        try:
            paciente = Paciente.objects.get(cpf=username)
            user = paciente.user 
            if user.check_password(password): 
                return user
        except Paciente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
