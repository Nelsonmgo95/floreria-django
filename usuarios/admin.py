from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Usuarios


class Administrador(UserAdmin):
    list_display = ('email', 'nombre', 'apellido', 'username', 'ultimo_login', 'fecha_creacion', 'is_active')
    list_display_links = ('email' , 'nombre', 'apellido')
    readonly_fields = ('ultimo_login', 'fecha_creacion')
    ordering = ('-fecha_creacion',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

# Register your models here.
admin.site.register(Usuarios, Administrador)