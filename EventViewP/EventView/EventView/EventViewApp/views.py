from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin #esto es el control para que no se mentan en paginas sin estar logeados

# Create your views here.



def cargar_inicio(request):
    return render(request, "EventViewApp/index.html")

def a(request):
    return render(request,"EventViewApp/a.html")


