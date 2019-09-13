from django.urls import path
from .views import (cargar_inicio,a,LoginView, LogoutView)

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('a/',a,name ='a'),

    path('iniciosesion', LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logoutsesion', LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),

]