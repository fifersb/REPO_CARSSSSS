from django.shortcuts import render
from .models import SliderIndex, FotosGaleria, MisionVision, FormInsumo

#----------------------------------------------
from django.contrib.auth.models import User
#---------------------------------------------------------------------------------
from django.contrib.auth import authenticate, logout, login as login_autent
#-----------------------------------------------
from django.contrib.auth.decorators import login_required,permission_required

#---------------------------------------------------------------------------------
# Create your views here.
def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'WEB/index.html', {'autos':autos})

@login_required(login_url='/login/')
def galeria(request):
    fotos = FotosGaleria.objects.all()
    return render(request,'WEB/galeria.html', {'fotos':fotos})

def quienes(request):
    info = MisionVision.objects.all()
    return render(request,'WEB/QuieneSomos.html', {'Info':info})

def ubicacion(request):
    return render(request,'WEB/Ubicacion.html')


def FormUsuario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtapellido")
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtNomuser")
        password = request.POST.get("txtPass")
        try:
            u = User.objects.get(username=usuario)
            return render(request,'WEB/FormularioUsuario.html',{'msg':'usuario existente'}) 
        except:
         
            u = User()
            u.username = usuario
            u.first_name = nombre
            u.last_name = apellido
            u.email =  email
            u.set_password(password)
            u.save()

            us= authenticate(request, username=usuario,password=password)
            login_autent(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'WEB/index.html', {'user':us,'autos':autos})

    return render(request,'WEB/FormularioUsuario.html')

@login_required(login_url='/login/')
@permission_required('riperCars.change_insumos',login_url='/login/')
def modificar_insumo(request):
    if request.POST:
        nombre=request.POST.get("txtNombreInsumo")
        precio=request.POST.get("txtPrecio")
        descripcion=request.POST.get("txtDescripcion")
        stock=request.POST.get("txtStock")

        try:
            ins = FormInsumo.objects.get(nombre=nombre)
            ins.precio = precio
            ins.descripcion = descripcion
            ins.stock = stock
            ins.save()
            msg='Datos Acutalizados'
        except:
            msg='No Existe Insumo'
        insu = FormInsumo.objects.all()
        return render(request,'web/admin_Insumos.html',{'lista_insumos':insu,'msg':msg})

@login_required(login_url='/login/')
@permission_required('riperCars.view_insumos',login_url='/login/')
def buscar_insumo(request,id):
    try:
        ins = FormInsumo.objects.get(nombre=id)
        return render(request,'web/Form_Insu_mod.html',{'insumo':ins}) 
    except:
        msg='No Encontro Insumo'
    insu = FormInsumo.objects.all()
    return render(request,'web/admin_Insumos.html',{'lista_insumos':insu,'msg':msg})

@login_required(login_url='/login/')
@permission_required('riperCars.view_insumos',login_url='/login/')
@permission_required('riperCars.delete_insumos',login_url='/login/')
def eliminar(request,id):
    try:
        ins = FormInsumo.objects.get(nombre=id)
        ins.delete()
        msg='Eliminado'
    except:
        msg='No fue Eliminado'
    insu = FormInsumo.objects.all()
    return render(request,'web/admin_Insumos.html',{'lista_insumos':insu,'msg':msg})

@login_required(login_url='/login/')
@permission_required('riperCars.view_insumos',login_url='/login/')
def admin_insumos(request):
    insu = FormInsumo.objects.all()
    return render(request,'web/admin_Insumos.html',{'lista_insumos':insu})

@login_required(login_url='/login/')
@permission_required('riperCars.add_insumos',login_url='/login/')
def FormInsumos(request):
    if request.POST:
        nombre=request.POST.get("txtNombreInsumo")
        precio=request.POST.get("txtPrecio")
        descripcion=request.POST.get("txtDescripcion")
        stock=request.POST.get("txtStock")
        ins = FormInsumo(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        ins.save()

        return render(request,'WEB/FormularioInsumos.html',{'msg':'Insumo Registrado'})
    return render(request,'WEB/FormularioInsumos.html')




def logout_vista(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'WEB/index.html', {'autos':autos})

def login(request):
    if request.POST:
        usuario= request.POST.get("txtuser")
        password= request.POST.get("txtPass")
        us= authenticate(request, username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'WEB/index.html', {'user':us,'autos':autos})
        else:
            return render(request,'WEB/index.html',{'msg':'usuario/ pass incorrecta'})

    return render(request,'WEB/login.html')
