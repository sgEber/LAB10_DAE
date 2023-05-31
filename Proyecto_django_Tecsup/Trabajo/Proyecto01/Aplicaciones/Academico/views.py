from django.shortcuts import render,redirect
from .models import Curso,Docente,Especialidad,Matricula
from django.contrib.auth import authenticate, login

# Create your views here.

def logeo(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            CursoListado = Curso.objects.order_by('codigo')
            return render(request, 'gestionCursos.html', {"cursos":CursoListado}) 
        else:
            # El usuario no ha proporcionado credenciales válidas
            pass
    return render(request,'Login.html')

#cursos
def Cursos(request):
    cursosListado=Curso.objects.all()
    return render(request,"GestionCursos.html",{"cursos":cursosListado})

def registrarcurso(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/curso')

def edicioncurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    context = {
        'curso': curso
    }
    return render(request, 'edicionCurso.html', context)

def editarCurso(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    creditos = request.POST["numcreditos"]

    curso = Curso.objects.get(codigo = codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/curso')

def eliminarcurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/curso')

def buscarCurso(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Curso.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'buscarCurso.html',{"curso":busqueda})
    else:
        cursosListado = Curso.objects.all()
        return render(request, "buscarCurso.html",{"curso":cursosListado})


#Docentes

def Docentes(request):
    docentesListado = Docente.objects.all()
    cursosListado = Curso.objects.all()
    context = {
        "docentes": docentesListado,
        "cursos": cursosListado
    }
    return render(request, "GestionDocentes.html", context)

def registrardocente(request):
    IdDocente=request.POST["txtIdDocente"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    FIngreso=request.POST["dateFIngreso"]
    Dni=request.POST["txtDni"]
    Telefono=request.POST["numTelefono"]
    Curso = request.POST["sCurso"]  # Obtiene el valor seleccionado del campo de selección "Curso"

    docente = Docente.objects.create(IdDocente=IdDocente, Nombre=Nombre, Apellido=Apellido, FIngreso=FIngreso, Dni=Dni, Telefono=Telefono, Curso_id=Curso)
    return redirect('/docente')

def eliminardocente(request,IdDocente):
    docente=Docente.objects.get(IdDocente=IdDocente)
    docente.delete()
    return redirect('/docente')

def buscarDocentes(request):
    if request.method == "POST":
        buscarfingreso = request.POST.get('fingreso')
        busqueda=Docente.objects.filter(FIngreso__icontains=buscarfingreso)
        return render(request,'buscarDocente.html',{"docente":busqueda})
    else:
        docentesListado = Docente.objects.all()
        return render(request, "buscarDocente.html",{"docente":docentesListado})
    
def edicionDocente(request, IdDocente):
    docentesListado = Docente.objects.get(IdDocente=IdDocente)
    cursosListado = Curso.objects.all()
    context = {
        "docente": docentesListado,
        "curso": cursosListado
    }
    return render(request, "edicionDocente.html",context)

def editarDocente(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    fingreso = request.POST["txtfingreso"]
    dni = request.POST["txtdni"]
    telefono = request.POST["numtelefono"]

    docente = Docente.objects.get(IdDocente = codigo)
    docente.Nombre = nombre
    docente.Apellido = apellido
    docente.FIngreso = fingreso
    docente.Dni = dni
    docente.Telefono = telefono
    docente.save()

    return redirect('/docente')

#Especialidades

def Especialidades(request):
    especialidadesListado = Especialidad.objects.all()
    cursosListado = Curso.objects.all()
    context = {
        "especialidades": especialidadesListado,
        "cursos": cursosListado
    }
    return render(request, "GestionEspecialidades.html", context)

def registrarespecialidad(request):
    IdEspecialidad = request.POST["txtIdEspecialidad"]
    Nombre = request.POST["txtNombre"]
    Descripcion = request.POST["txtDescripcion"]
    Curso = request.POST["sCurso"]

    especialidad = Especialidad.objects.create(IdEspecialidad=IdEspecialidad, Nombre=Nombre, Descripcion=Descripcion, Curso_id=Curso)
    return redirect('/especialidad')

def eliminarespecialidad(request, IdEspecialidad):
    especialidad = Especialidad.objects.get(IdEspecialidad=IdEspecialidad)
    especialidad.delete()
    return redirect('/especialidad')

def buscarEspecialidad(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Especialidad.objects.filter(Nombre__icontains=buscarnombre)
        return render(request,'buscarEspecialidad.html',{"especialidad":busqueda})
    else:
        especialidadListado = Especialidad.objects.all()
        return render(request, "buscarEspecialidad.html",{"especialidad":especialidadListado})

def edicionEspecialidad(request, IdEspecialidad):
    especialidad = Especialidad.objects.get(idEspecialidad = IdEspecialidad)
    return render(request, "edicionEspecialidad.html",{"especialidad":especialidad})

def editarEspecialidad(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    especialidad = Especialidad.objects.get(idEspecialidad = codigo)
    especialidad.nombre = nombre
    especialidad.descripcion = descripcion
    especialidad.save()

    return redirect('/especialidad')

#MAtriculas

def Matriculas(request):
    MatriculasListado = Matricula.objects.all()
    cursosListado = Curso.objects.all()
    context = {
        "matriculas": MatriculasListado,
        "cursos": cursosListado
    }
    return render(request, "GestionMatricula.html", context)

def registrarmatricula(request):
    IdMatricula=request.POST["IdMatricula"]
    IdCurso=request.POST["sCurso"]
    Fechamat=request.POST["dateMat"]
    Cuotas = request.POST["numcuotas"]

    matricula=Matricula.objects.create(IdMatricula=IdMatricula, IdCurso_id=IdCurso, Fechamat=Fechamat, Cuotas=Cuotas)
    return redirect('/matricula')

def eliminarMatricula(request,IdMatricula):
    matricula=Matricula.objects.get(IdMatricula=IdMatricula)
    matricula.delete()
    return redirect('/matricula')

def buscarMatricula(request):
    if request.method == "POST":
        buscarMingreso = request.POST.get('fechaMatricula')
        matricula=Matricula.objects.filter(Fechamat__icontains=buscarMingreso)
        return render(request,'buscarMatricula.html',{"matricula":matricula})
    else:
        matriculaListado = Matricula.objects.all()
        return render(request, "buscarMatricula.html",{"matricula":matriculaListado})

def edicionmatricula(request, IdMatricula):
    matricula = Matricula.objects.get(IdMatricula = IdMatricula)
    cursosListado=Curso.objects.all()
    context = {
        "matricula": matricula,
        "cursos": cursosListado
    }
    return render(request, "edicionMatricula.html",context)


def editarMatricula(request):
    IdMatricula = request.POST["txtcodigo"]
    Fechamat = request.POST["fechamat"]
    Cuotas = request.POST["numcuotas"]
    codigo_curso = request.POST["sCurso"]
    
    curso = Curso.objects.get(codigo=codigo_curso) 
    matricula = Matricula.objects.get(IdMatricula=IdMatricula)
    matricula.Fechamat = Fechamat
    matricula.Cuotas = Cuotas
    matricula.IdCurso = curso 
    matricula.save()
    return redirect('/matricula')