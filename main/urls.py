from django.urls import path, include
from . import views

app_name='main' ### necesario para poner en el views.py y redirreccionar

##junto con el de: views.homepage, name='homepage'),

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registro/', views.register, name='registro'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
]