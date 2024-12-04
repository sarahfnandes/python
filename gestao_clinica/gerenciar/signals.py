# signals.py

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Paciente

@receiver(post_save, sender=Paciente)
def criar_usuario_para_paciente(sender, instance, created, **kwargs):
    if created and not instance.user:  # Se o paciente for criado e não tem um usuário associado
        user = User.objects.create_user(
            username=instance.cpf,  # Usando o CPF do paciente como username
            password="essenza"  # Senha padrão
        )
        instance.user = user
        instance.save()  # Salva novamente o paciente com o usuário associado
