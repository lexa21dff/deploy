from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.lista_inscritos import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


from django.shortcuts import get_object_or_404

from proyectos.views.funciones import *

class AgregarIntegrantesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_inscritos(self, request, *args, **kwargs):
        # Obtener el perfil_id de los argumentos de la solicitud
        perfil_id = kwargs['id_user']

        # Obtener los inscritos que coinciden con el perfil_id y cumplen las condiciones
        inscritos = Inscrito.objects.filter(perfil_id=perfil_id, estado='activo', nombre_grupo__isnull=True)

        # Obtener todas las fichas asociadas a los inscritos
        fichas = inscritos.values_list('ficha', flat=True).distinct()

        # Filtrar los inscritos que tienen alguna de las fichas asociadas
        # Filtrar los inscritos que tienen alguna de las fichas asociadas y cumplen las condiciones adicionales
        inscritos_misma_ficha = Inscrito.objects.filter(ficha__in=fichas, estado='activo', nombre_grupo__isnull=True)

        
        # Serializar los datos de los inscritos
        serializer = self.get_serializer(inscritos_misma_ficha, many=True)

        # Devolver la respuesta con los datos serializados
        return Response(serializer.data)