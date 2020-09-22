from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListadoAutor, ActualizarAutor, CrearAutor, EliminarAutor, AutorViewSet

router = DefaultRouter()
router.register(r'api/v1.0', AutorViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('crear_autor/',CrearAutor.as_view(), name = 'crear_autor'),
    path('listar_autor/',ListadoAutor.as_view(), name = 'listar_autor'),
    path('editar_autor/<int:pk>',ActualizarAutor.as_view(), name = 'editar_autor'),
    path('eliminar_autor/<int:pk>',EliminarAutor.as_view(), name = 'eliminar_autor'),
]
