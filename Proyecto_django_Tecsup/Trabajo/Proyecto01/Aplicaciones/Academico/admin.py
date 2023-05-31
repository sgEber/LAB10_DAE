from django.contrib import admin

# Register your models here.

from .models import Curso,Docente,Especialidad,Matricula



class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre','creditos')

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('IdDocente', 'Apellido','Nombre','FIngreso','Dni','Telefono','Curso')

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('IdEspecialidad','Nombre','Descripcion','Curso')

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('IdMatricula','IdCurso','Fechamat','Cuotas')




admin.site.register(Curso,CursoAdmin)
admin.site.register(Docente,DocenteAdmin)
admin.site.register(Especialidad,EspecialidadAdmin)
admin.site.register(Matricula,)