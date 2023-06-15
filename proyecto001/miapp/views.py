from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo

# Create your views here.
layout = """
<h1> Proyecto Web (LP3) | Edwin Paucar </h1>
<hr/>
<ul>
<li>
<a href="/inicio"> Inicio</a>
</li>
<li>
<a href="/saludo"> Mensaje de Saludo</a>
</li>
<li>
<a href="/rango"> Mostrar Números [a,b]</a>
</li>
<li>
<a href="/rango2/10/15"> Mostrar Números [10,15]</a>
</li>
<li>
<a href="/crear-articulo"> Mostrar Articulos</a>
</li>
</ul>

<hr/>
"""
def index(request):
    return render(request,'index.html')

def saludo(request):
    return render(request,'saludo.html')

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
'titulo':'Rango',
'a':a,
'b':b,
'rango_numeros':rango_numeros
})

def rango2(request,a=40,b=10):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
<h2> Números de [{a},{b}] </h2>
"""
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)


def index(request):
    return render(request,'index.html', {
    'titulo':'Inicio',
    'mensaje':'Proyecto web con DJango (Desde el View)'
})

def saludo(request):
    return render(request,'saludo.html',{
    'titulo':'Saludo',
    'autor_saludo':'Edwin Manuel Paucar Nonajulca'
})

def index(request):
    return render(request,'index.html', {
    'titulo':'Inicio',
})


def index(request):
    estudiantes = [ 'Isabella Caballero',
'Alejandro Hermitaño',
'Joan Palomino',
'Pierre Bernaola',
'Danne Barzola']

    return render(request,'index.html', {
'titulo':'Inicio',
'mensaje':'Proyecto Web Con DJango',
'estudiantes': estudiantes
})

def crear_articulo(request,titulo, contenido, publicado):
    articulo = Articulo(
        titulo = 'titulo',
        contenido = contenido,
        publicado = publicado
        )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=1000)
        resultado = f"""Articulo:
        <br> <strong>ID:</strong> {articulo.id}
        <br> <strong>Título:</strong> {articulo.titulo}
        <br> <strong>Contenido:</strong> {articulo.contenido}
        """
    except:
        resultado = "<h1> Artículo No Encontrado </h1>"
    return HttpResponse(resultado)
