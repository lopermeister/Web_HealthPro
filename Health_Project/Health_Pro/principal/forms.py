from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ('no_afiliacion','clinica','tipo_sangre','p_fecha_nacimiento','p_curp','slug')


class DotctorForm(forms.Form):
    model = Doctores
    fields = "__all__"
