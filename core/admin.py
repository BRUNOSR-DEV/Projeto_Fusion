from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Recursos


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificados')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificados' )

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificados', 'ativo')

@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone', 'modificados', 'ativo')


