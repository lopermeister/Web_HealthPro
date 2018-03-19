from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pacientes(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    no_afiliacion = models.CharField(max_length =20)
    clinica = models.ForeignKey('Clinicas', on_delete = models.CASCADE)
    estatus = models.BooleanField(default = False)
    fecha_registro = models.DateField(auto_now_add=True)
    tipo_sangre= models.CharField(max_length=5)
    slug = models.SlugField(max_length=24,default ="Paciente_Generico")
    p_curp= models.CharField(max_length=15)
    p_fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.user.username

class Clinicas(models.Model):
    id_clinica = models.IntegerField()
    clinica = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return str(self.id_clinica)

class Consultorios(models.Model):
    id_consultorio = models.IntegerField()
    consultorio_numero = models.IntegerField(default=0)
    clinca = models.ForeignKey(Clinicas,on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.id_consultorio


class Doctores(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    d_curp = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=50)
    d_rfc = models.CharField(max_length=13)
    fecha_nacimiento = models.DateField()
    estatus = models.BooleanField(default= True)
    def __str__(self):
        return self.user.username

class Medicamentos(models.Model):
    id_medicamento = models.CharField(max_length=25)
    medicamento_name= models.CharField(max_length= 50, default="X")
    marca = models.CharField(max_length=50)
    formula = models.CharField(max_length=50)
    vida_media = models.CharField(max_length=50)
    peso_mol = models.FloatField()
    prescrito = models.BooleanField(default= False)

class Medicamentos_Pacientes(models.Model):
    paciente = models.ForeignKey('Pacientes',on_delete=models.CASCADE)
    id_medicamento = models.ManyToManyField(Medicamentos)
    fecha_expedicion = models.DateField()
    resurtir = models.BooleanField(default = False)

class Doctores_Consultorios(models.Model):
    doctor = models.ForeignKey('Pacientes',on_delete=models.CASCADE)
    consultorio = models.ForeignKey('Consultorios', on_delete=models.CASCADE)
    horario = models.CharField(max_length=50)

class Citas(models.Model):
    paciente = models.ForeignKey('Pacientes',on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctores',on_delete=models.CASCADE)
    cita_fecha_hora = models.DateTimeField()
    estatus = models.BooleanField(default = True)
    consultorio = models.CharField(max_length=25)

class Consultas(models.Model):
    paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE)
    medico = models.ManyToManyField(Doctores)
    cita = models.ForeignKey(Citas,on_delete=models.CASCADE)
    consulta_fecha_hora = models.DateTimeField(auto_now_add=True)
    Sintomas = models.CharField(max_length=250)
    Notas = models.CharField(max_length=250)
    receta = models.ForeignKey(Medicamentos_Pacientes,on_delete=models.CASCADE)
