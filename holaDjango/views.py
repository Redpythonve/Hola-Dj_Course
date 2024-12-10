from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")


def despedida(request):
    return HttpResponse("Chao Mundo")

def adulto (request, edad):
    if edad >= 18:
      return HttpResponse("Eres Mayor de Edad")
    else:
       return HttpResponse("Eres Menor de Edad")