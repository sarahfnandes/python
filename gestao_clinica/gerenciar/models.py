from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  
    email = models.EmailField()
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)
    historico_medico = models.TextField(null=True, blank=True)  # Certifique-se de que esta linha está corretamente indentada
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    convenio_saude = models.CharField(max_length=50)
    codigo_convenio = models.CharField(max_length=30, unique=True)
    plano_saude = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


@receiver(post_save, sender=Paciente)
def create_user_for_paciente(sender, instance, created, **kwargs):
    if created:
        # Cria um usuário com o CPF do paciente como nome de usuário
        user = User.objects.create_user(username=instance.cpf, password="essenza")
        # Associa o usuário criado ao paciente
        instance.user = user
        instance.save()

@receiver(post_save, sender=Paciente)
def save_user_for_paciente(sender, instance, **kwargs):
    instance.user.save()

class Especialidade(models.Model):
    especializacao = models.CharField(max_length=100)

    def __str__(self):
        return self.especializacao

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome


class Convenio(models.Model):
    nome_convenio = models.CharField(max_length=100)
    tipo_convenio = models.CharField(max_length=50)
    numero_convenio = models.CharField(max_length=30)
    validade = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_convenio
class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('Agendado', 'Agendado'),
        ('Confirmado', 'Confirmado'),
        ('Retorno', 'Retorno'),
    ]
    data_horario = models.DateTimeField()
    tipo_consulta = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Agendamento: {self.tipo_consulta} - {self.paciente.nome}"



@receiver(post_save, sender=Paciente)
def create_user_for_paciente(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.cpf, password="essenza")
        # Defina outros campos do usuário se necessário
        user.save()
