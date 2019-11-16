from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):               # Primera vista. Recibe un request como primer argumento de esta funcion
    
    doc_externo=open("C:/Users/Simón/Desktop/Programacion/PROYECTO_DJANGO/Proyecto1/Proyecto1/PlantillasDJ/miPlantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta muy pronto")

def damefecha(request):

    fecha_actual=datetime.datetime.now()
    
    documento="""
    FECHA Y HORA ACTUALES: %s               # marcador de posición para ver fecha y hora
    """ % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,anio):

    periodo=anio-2019
    edadFutura=edad+periodo
    documento="<html><body><h2> En el año %s tendrás %s años" %(anio, edadFutura)

    return HttpResponse(documento)