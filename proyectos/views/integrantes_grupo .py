from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from proyectos.serializers.lista_inscritos import ListaInscritoSerializer
from proyectos.models import Inscrito, Proyecto

class IntegrantesDelGrupoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer

    @action(detail=False, methods=['get'])
    def get_mis_grupos(self, request, *args, **kwargs):
        proyecto_id = kwargs['id_proyecto']

        # Retrieve the proyecto with proyecto_id
        proyecto = get_object_or_404(Proyecto, id=proyecto_id)

        # Retrieve the inscrito with id = proyecto.aprendiz
        inscrito = get_object_or_404(Inscrito, id=proyecto.aprendiz.id)

        # Filter the inscritos with the same nombre_grupo as the found inscrito
        inscritos = Inscrito.objects.filter(nombre_grupo_id=inscrito.nombre_grupo_id)

        # Serialize the data of the inscritos
        serializer = self.get_serializer(inscritos, many=True)
        return Response(serializer.data)
