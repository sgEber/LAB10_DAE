from django.urls import path
from . import views

urlpatterns = [

    path('',views.logeo),

    path('curso',views.Cursos,name='curso'),
    path('registrarcurso',views.registrarcurso),
    path('eliminarcurso/<codigo>',views.eliminarcurso),
    path('edicioncurso/<str:codigo>/', views.edicioncurso, name='edicioncurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),
    path('buscarCurso', views.buscarCurso, name= 'buscarCurso'),

    path('docente',views.Docentes,name='docente'),
    path('registrardocente',views.registrardocente),
    path('ediciondocente/<str:IdDocente>', views.edicionDocente),
    path('editarDocente/', views.editarDocente,name='editarDocente'),
    path('eliminardocente/<IdDocente>',views.eliminardocente),
    path('buscarDocentes', views.buscarDocentes, name= 'buscarDocentes'),

    path('especialidad',views.Especialidades,name='especialidad'),
    path('registrarespecialidad',views.registrarespecialidad),
    path('edicionespecialidad/<str:IdEspecialidad>/', views.edicionEspecialidad),
    path('editarespecialidad', views.editarEspecialidad),
    path('eliminarespecialidad/<IdEspecialidad>',views.eliminarespecialidad),
    path('buscarEspecialidad', views.buscarEspecialidad, name= 'buscarEspecialidad'),

    path('matricula',views.Matriculas,name='matricula'),
    path('registrarmatricula',views.registrarmatricula),
    path('eliminarmatricula/<IdMatricula>',views.eliminarMatricula),
    path('buscarMatricula', views.buscarMatricula, name= 'buscarMatricula'),
    path('edicionmatricula/<str:IdMatricula>/', views.edicionmatricula, name='edicionmatricula'),
    path('editarMatricula/', views.editarMatricula, name='editarMatricula'),



]