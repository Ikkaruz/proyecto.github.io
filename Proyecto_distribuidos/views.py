from django.shortcuts import render,redirect
from base.models import *

est = Estudiante()
prest = Prestamo()
impl = Implemento()

def home(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def implements(request):
    return render(request, 'implementos.html')

def pending(request):
    cookie = readCookie(request)
    login = cookie[0]
    password = cookie[1]
    estudiante = est.findEst(login, password)
    pend = prest.findPending(estudiante.cedula)
    if pend == False:
        return redirect(home)
    elif pend != None and pend != False:
        implement = impl.buscarExistencias(pend.implemento)
        datos = {
            'nombre': implement.nombre,
        }
        return render(request, 'pendientes.html', datos)
    return redirect(sign_in)

def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        pss = request.POST['pass']
        estudiante = est.findEst(user=user, passw=pss)
        values = user+','+pss
        if estudiante != None:
            prestamo = prest.findPending(estudiante.cedula)
            if prestamo:
                response = redirect(pending)
                response.set_cookie('login', values)
                return response
            else:
                response = redirect(implements)
                response.set_cookie('login', values)
                return response
        else:
            return redirect(sign_in)
    else:
        print('')

def readCookie(request):
    cookie = request.COOKIES.get('login')
    values = str(cookie)
    x = values.replace("'", "")
    return x.split(',')

def createPending(request):
    y = readCookie(request);
    user = y[0]
    pasw = y[1]
    if request.method == 'POST' and 'baloncesto' in request.POST:
        if user != None and pasw != None:
            estudiante = est.findEst(user=user, passw=pasw)
            implemento = impl.buscarExistencias(nombre='balon_baloncesto')
            existencias = int(implemento.cantidad_disponible)
            prestamo = prest.findPending(estudiante.cedula)
            if existencias > 0 and prestamo == False:
                prest.CreatePending(estudiante=estudiante.cedula, implemento=implemento.nombre)
                return redirect(pending)
            else:
                return redirect(pending)
        else:
            print('ta vacia la cookie')

    if request.method == 'POST' and 'futbol' in request.POST:
        if user != None and pasw != None:
            estudiante = est.findEst(user=user, passw=pasw)
            implemento = impl.buscarExistencias(nombre='balon_futbol')
            existencias = int(implemento.cantidad_disponible)
            prestamo = prest.findPending(estudiante.cedula)
            if existencias > 0 and prestamo == False:
                prest.CreatePending(estudiante=estudiante.cedula, implemento=implemento.nombre)
                return redirect(pending)
            else:
                return redirect(pending)
        else:
            print('ta vacia la cookie')

    if request.method == 'POST' and 'micro' in request.POST:
        if user != None and pasw != None:
            estudiante = est.findEst(user=user, passw=pasw)
            print(estudiante.cedula)
            implemento = impl.buscarExistencias(nombre='balon_micro')
            existencias = int(implemento.cantidad_disponible)
            prestamo = prest.findPending(estudiante.cedula)
            if existencias > 0 and prestamo == False:
                prest.CreatePending(estudiante=estudiante.cedula, implemento=implemento.nombre)
                return redirect(pending)
            else:
                return redirect(pending)
        else:
            print('ta vacia la cookie')

    if request.method == 'POST' and 'ajedrez' in request.POST:
        if user != None and pasw != None:
            estudiante = est.findEst(user=user, passw=pasw)
            print(estudiante.cedula)
            implemento = impl.buscarExistencias(nombre='ajedrez')
            existencias = int(implemento.cantidad_disponible)
            prestamo = prest.findPending(estudiante.cedula)
            if existencias > 0 and prestamo == False:
                prest.CreatePending(estudiante=estudiante.cedula, implemento=implemento.nombre)
                return redirect(pending)
            else:
                return redirect(pending)
        else:
            print('ta vacia la cookie')

    if request.method == 'POST' and 'parchis' in request.POST:
        if user != None and pasw != None:
            estudiante = est.findEst(user=user, passw=pasw)
            print(estudiante.cedula)
            implemento = impl.buscarExistencias(nombre='parchis')
            existencias = int(implemento.cantidad_disponible)
            prestamo = prest.findPending(estudiante.cedula)
            if existencias > 0 and prestamo == False:
                prest.CreatePending(estudiante=estudiante.cedula, implemento=implemento.nombre)
                return redirect(pending)
            else:
                return redirect(pending)
        else:
            print('ta vacia la cookie')

    if request.method == 'POST' and 'jenga' in request.POST:
        if user != None and pasw != None:
            estudiante = est.findEst(user=user, passw=pasw)
            print(estudiante.cedula)
            implemento = impl.buscarExistencias(nombre='jenga')
            existencias = int(implemento.cantidad_disponible)
            prestamo = prest.findPending(estudiante.cedula)
            if existencias > 0 and prestamo == False:
                prest.CreatePending(estudiante=estudiante.cedula, implemento=implemento.nombre)
                return redirect(pending)
            else:
                return redirect(pending)
        else:
            print('ta vacia la cookie')

    if request.method == 'POST' and 'pingpong' in request.POST:
        if user != None and pasw != None:
            estudiante = est.findEst(user=user, passw=pasw)
            print(estudiante.cedula)
            implemento = impl.buscarExistencias(nombre='raquetas_ping_pong')
            existencias = int(implemento.cantidad_disponible)
            prestamo = prest.findPending(estudiante.cedula)
            if existencias > 0 and prestamo == False:
                prest.CreatePending(estudiante=estudiante.cedula, implemento=implemento.nombre)
                return redirect(pending)
            else:
                return redirect(pending)
        else:
            print('ta vacia la cookie')

    return redirect(home)

def deletePending(request):
    cookie = readCookie(request)
    estudiante = est.findEst(cookie[0], cookie[1])
    prest.anulatePending(estudiante.cedula)
    return redirect(home)
