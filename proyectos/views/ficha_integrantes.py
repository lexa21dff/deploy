from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from proyectos.models import Inscrito, Proyecto, Entrega
from proyectos.serializers.lista_inscritos import *

class FichaIntegrantesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer

    @action(detail=True, methods=['get'])
    def get_ficha_integrantes(self, request, *args, **kwargs):
        ficha_id = kwargs['ficha_id']
        inscritos = Inscrito.objects.filter(ficha_id=ficha_id)
        serializer = self.get_serializer(inscritos, many=True)
        return Response(serializer.data)