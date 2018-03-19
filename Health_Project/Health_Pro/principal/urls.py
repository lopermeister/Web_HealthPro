from django.urls import path
from principal import views
from .views import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns= [
    #path('paciente/mis_medicamentos/',view.medicamentos_paciente_view,name="mis_medicamentos"),
    path('paciente/nuevo_paciente/',Nuevo_paciente.as_view(),name="nuevo_paciente_view"),
    path('signup/',views.signup, name="signup"),
    path('medicos/nuevo_medico/',Nuevo_doctor.as_view(),name="nuevo_medico_view "),
    path('login/',login,{'template_name':'common/login.html'},name="login"),
    path('logout_then_login/',logout_then_login,name="logout_then_login"),
]
