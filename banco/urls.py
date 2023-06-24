"""Banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proyectos.views.login import UserLoginAPIView
from proyectos.views.signup import UserSignUpAPIView
from proyectos.views.lista_proyecto import *
from proyectos.views.lista_entrega import *
from proyectos.views.lista_inscritos import ListaInscritosViewSet
from proyectos.views.lista_grupos import *
from proyectos.views.Instructor_proyectos import  *
from proyectos.views.agregar_integrantes import *
from proyectos.views.integrantes import IntegrantesViewSet


from proyectos.views.estado_proyecto import obtener_estados_proyecto
from proyectos.views.calificar_proyecto import CalificaProyectoViewSet
from proyectos.views.ficha_instructor import FichaInstructorViewSet
from proyectos.views.calificacion_dell_proyecto import ListaDeProyectosViewSet
from proyectos.views.ficha_integrantes import FichaIntegrantesViewSet
from proyectos.views.buscar_proyectos import ProyectoList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('proyectos.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/signup/', UserSignUpAPIView.as_view(), name='login'),
    path('buscar_proyectos/', ProyectoList.as_view()),
    # aprendiz 
    path('api/proyectos/<int:id_user>/',ListaProyectosViewSet.as_view({'get':'get_usuario_proyectos'}), name='aprendiz'),
    # path('api/proyectos/<int:id_user>/',IntegrantesDelGruposViewSet.as_view({'get':'get_usuario_proyectos'}), name='aprendiz'),
    path('api/entregas/<int:id_proyecto>/', ListaEntregaViewSet.as_view({'get': 'get_entregas_por_proyecto'}), name='lista_entregas_por_proyecto'),
    # instructor
    path('api/calificar-proyecto/<int:proyecto_id>/<str:estado>/', CalificaProyectoViewSet.as_view({'put': 'actualizar_proyecto'}), name='instructor'),
    # grupos
    path('api/inscritos/<int:id_user>/', ListaInscritosViewSet.as_view({'get': 'get_inscritos'}), name='inscritos_ficha'),
    path('api/grupos/<int:id_user>/', ListaGruposViewSet.as_view({'get': 'get_mis_grupos'}), name='mis_grupos'),
    path('api/agregar-integrantes/<int:id_user>/', AgregarIntegrantesViewSet.as_view({'get': 'get_inscritos'}), name='get_fichas_usuario'),
    path('api/integrantes/<int:grupo_id>/', IntegrantesViewSet.as_view({'get': 'get_integrantes'}), name='get_fichas_usuario'),


    path('api/obtener-estados-proyecto/', obtener_estados_proyecto, name='obtener_estados_proyecto'),
    path('api/proyectos-instructor/<int:ficha_id>/',ProyectosViewSet.as_view({'get':'get_usuario_proyectos'}), name='entregas_por_usuario_proyecto'),
    path('api/fichas-instructor/<int:id_user>/',FichaInstructorViewSet.as_view({'get':'get_fichas'}), name='fichas_instructor'),
    path('api/fichas-integrantes/<int:ficha_id>/',FichaIntegrantesViewSet.as_view({'get':'get_ficha_integrantes'}), name='fichas_Integrantes'),

    path('proyectos/ficha/<int:ficha_id>/', ListaDeProyectosViewSet.as_view({'get': 'get_usuario_proyectos'}), name='get_usuario_proyectos'),

]

