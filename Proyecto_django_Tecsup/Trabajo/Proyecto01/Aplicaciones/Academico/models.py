from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.codigo}{self.nombre}{self.creditos}"

class Docente(models.Model):
    IdDocente = models.CharField(primary_key=True,max_length=6)
    Apellido = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    FIngreso = models.DateField(auto_now_add=True)
    Dni = models.CharField(max_length=8)
    Telefono = models.IntegerField()
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.IdDocente}{self.Apellido}{self.Nombre}{self.FIngreso}{self.Dni}{self.Telefono}{self.Curso.nombre}"

class Especialidad (models.Model):
    IdEspecialidad = models.CharField(primary_key=True,max_length=6)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.IdEspecialidad}{self.Nombre}{self.Descripcion}{self.Curso.nombre}"

class Matricula (models.Model):
    IdMatricula = models.CharField(primary_key=True,max_length=6)
    IdCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Fechamat = models.DateField()
    Cuotas = models.IntegerField()

    def __str__(self):
        return f"{self.IdMatricula}{self.IdCurso}{self.Fechamat}{self.Cuotas}"