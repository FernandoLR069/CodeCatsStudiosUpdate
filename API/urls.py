from django.urls import path
from .views import CrearMensaje, VerMensajes, VerMensajePorId, EliminarMensaje, enviar_mensaje

urlpatterns = [
    path('enviar-mensaje/', enviar_mensaje, name='enviar_mensaje'),
]
