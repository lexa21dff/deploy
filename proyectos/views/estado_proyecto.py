from django.http import JsonResponse
from proyectos.models import ESTADO_PROYECTO

def obtener_estados_proyecto(request):
    estados = dict(ESTADO_PROYECTO)  # Convertir la tupla de estados en un diccionario
    return JsonResponse(estados)
