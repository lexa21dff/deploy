from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.proyecto import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from proyectos.models import Inscrito

class ListaProyectosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_usuario_proyectos(self, request, *args, **kwargs):
        perfil_id = kwargs['id_user']
        inscrito = Inscrito.objects.filter(perfil_id=perfil_id)
        grupo_ids = inscrito.values_list('nombre_grupo', flat=True)
        
        inscritos = Inscrito.objects.filter(nombre_grupo__id__in=grupo_ids)  # Filtra los inscritos por los IDs de los grupos
        
        integrante_ids = inscritos.values_list('id', flat=True)  # Obtén los IDs de los inscritos filtrados
    
        proyectos = Proyecto.objects.filter(aprendiz__id__in=integrante_ids)  # Filtra los proyectos por los IDs de los inscritos filtrados
    
        serializer = self.get_serializer(proyectos, many=True)
        return Response(serializer.data)


         


