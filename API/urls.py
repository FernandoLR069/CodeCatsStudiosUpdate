from django.urls import path
from .views import *

urlpatterns = [
    path('enviar-mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('enviar_mensaje_contacto/', enviar_mensaje_contacto, name='enviar_mensaje_contacto'),
    path('enviar_mensaje_contacto_web_desing_senpai/', enviar_mensaje_contacto_web_desing_senpai, name='enviar_mensaje_contacto_web_desing_senpai'),
    path('enviar_mensaje_contacto_web_desing_kaiju/', enviar_mensaje_contacto_web_desing_kaiju, name='enviar_mensaje_contacto_web_desing_kaiju'),
    path('enviar_mensaje_contacto_server_owncloud/', enviar_mensaje_contacto_server_owncloud, name='enviar_mensaje_contacto_server_owncloud'),
    path('enviar_mensaje_devs/', enviar_mensaje_devs, name='enviar_mensaje_devs'),
]
