from django.contrib import admin
from .models import Especialidade, Clinica, Medico, Paciente, Convenio, Agendamento

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'genero', 'data_nascimento', 'user')  # Exibe as colunas no Admin
    search_fields = ('nome', 'cpf', 'email')  # Permite buscar pelos campos especificados
    list_filter = ('genero',)  # Permite filtrar os pacientes por gênero no Admin

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('especializacao',)  # Exibe as especializações no Admin
    search_fields = ('especializacao',)

class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'email')
    search_fields = ('nome',)

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade', 'clinica')
    search_fields = ('nome', 'crm')

class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('nome_convenio', 'tipo_convenio', 'numero_convenio', 'validade')
    search_fields = ('nome_convenio',)

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('data_horario', 'tipo_consulta', 'status', 'medico', 'paciente')
    search_fields = ('status', 'tipo_consulta')

admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Clinica, ClinicaAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Convenio, ConvenioAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Paciente, PacienteAdmin)
