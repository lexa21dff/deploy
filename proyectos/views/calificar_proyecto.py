from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from proyectos.serializers.proyecto import ProyectoSerializer
from proyectos.models import Proyecto

class CalificaProyectoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['put'])
    def actualizar_proyecto(self, request, *args, **kwargs):
        id_proyecto = kwargs['proyecto_id']
        estado = kwargs['estado']
        
        try:
            proyecto = Proyecto.objects.get(id=id_proyecto)
            proyecto.estado = estado
            proyecto.save()
            
            return Response({'mensaje': 'Estado del proyecto actualizado correctamente'})
        except Proyecto.DoesNotExist:
            return Response({'error': 'El proyecto no existe'}, status=404)
