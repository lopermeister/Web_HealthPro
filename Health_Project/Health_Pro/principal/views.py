from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView#, IndexView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
# Create your views here.
def signup(request):
    #registered = False
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        pacienteform = PacienteForm(data=request.POST)
        if userform.is_valid() and pacienteform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            paciente = pacienteform.save(commit=False)
            paciente.user = user
            paciente.save()
   #        registered = True
        #else :
        #    `print (userform.errors,pacienteform.errors)
            return redirect('nuevo_paciente_view')
    else:
        userform = UserForm()
        pacienteform = PacienteForm()
    return render(request,'common/signup.html',{'userform':userform,'pacienteform':pacienteform})

class Reporte_mis_medicamentos(ListView):
    template_name = "pacientes/mis_medicamentos.html"
    model = Medicamentos_Pacientes

class Nuevo_paciente(CreateView):
    template_name = "pacientes/nuevo_paciente.html"
    model = Pacientes
    fields = "__all__"
    success_url = reverse_lazy("nuevo_paciente_view")

class Nuevo_doctor(CreateView):
    template_name = "medicos/nuevo_medico.html"
    model = Doctores
    fields = "__all__"
    success_url = reverse_lazy("nuevo_medico_view")
