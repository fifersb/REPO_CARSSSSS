from django.contrib import admin
from django.urls import path,include
from .views import index, galeria, quienes, ubicacion,FormUsuario, FormInsumos, login, logout_vista, admin_insumos, eliminar, buscar_insumo, modificar_insumo

urlpatterns = [
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='Gale'),
    path('quienes/',quienes,name='Quienes'),
    path('ubicacion/',ubicacion,name='Ubi'),
    path('FormUsuario/',FormUsuario,name='FormUsuario'),
    path('FormInsumos/',FormInsumos,name='FormInsumos'),
    path('login/',login,name='login'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('admin_insumos/',admin_insumos,name='ADMININSUMOS'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('buscar/<id>/',buscar_insumo,name='BUSCAR'),
    path('modificar/',modificar_insumo,name='MODIFICAR'),
]