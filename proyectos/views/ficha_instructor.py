from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.lista_inscritos import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from proyectos.models import Inscrito

class FichaInstructorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_fichas(self, request, *args, **kwargs):
        perfil_id = kwargs['id_user']
        inscrito = Inscrito.objects.filter(perfil_id=perfil_id)
        

        
        serializer = self.get_serializer(inscrito, many=True)
        return Response(serializer.data)