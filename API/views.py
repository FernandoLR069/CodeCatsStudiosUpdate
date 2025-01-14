from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .functions.fcSendMessageEmail import *
from .procedures import *
from django.shortcuts import render, redirect
from django.contrib import messages
@csrf_exempt

# Create your views here.
class CrearMensaje(APIView):
    def post(self, request):
        nombres = request.data.get('nombres')
        telefono = request.data.get('telefono')
        correo = request.data.get('correo')
        mensaje = request.data.get('mensaje')

        try:
            sp_crear_mensaje(nombres, telefono, correo, mensaje)
            return Response({'message': 'Mensaje creado exitosamente'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VerMensajes(APIView):
    def get(self, request):
        try:
            mensajes = sp_ver_mensajes()
            mensajes_json = [
                {
                    "id": mensaje[0],
                    "nombres": mensaje[1],
                    "telefono": mensaje[2],
                    "correo": mensaje[3],
                    "mensaje": mensaje[4]
                }
                for mensaje in mensajes
            ]
            return Response(mensajes_json, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VerMensajePorId(APIView):
    def get(self, request, id):
        try:
            mensaje = sp_ver_mensaje_id(id)
            if mensaje:
                mensaje_json = {
                    "id": mensaje[0],
                    "nombres": mensaje[1],
                    "telefono": mensaje[2],
                    "correo": mensaje[3],
                    "mensaje": mensaje[4]
                }
                return Response({'mensaje': mensaje_json}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Mensaje no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EliminarMensaje(APIView):
    def delete(self, request, id):
        try:
            sp_eliminar_mensaje(id)
            return Response({'message': 'Mensaje eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


def enviar_mensaje(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asent = request.POST.get('asent')
        proyect = request.POST.get('proyect')
        message = request.POST.get('message')

        # Verificar si todos los campos están completos
        if not name or not email or not telefono or not asent or not proyect or not message:
            # Si algún campo está vacío, redirigir a error404
            return redirect('error404')

        try:
            # Llamar a la función para enviar el mensaje (asegúrate de que esta función esté correctamente implementada)
            enviar_mensaje_formulario(name, email, telefono, asent, proyect, message)
            enviar_confirmacion_cliente(name, email)
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')

            # Redirigir a la página de contacto
            return redirect('contact')

        except Exception as e:
            # Si hay algún error al enviar el mensaje, redirigir a error404
            return redirect('error404')

    # Si el método no es POST, simplemente renderizar la página de contacto
    return render(request, 'contact.html')


def enviar_mensaje_contacto(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        # Verificar si todos los campos están completos
        if not name or not email or not telefono:
            # Si algún campo está vacío, redirigir a error404
            return redirect('error404')

        try:
            # Llamar a la función para enviar el mensaje (asegúrate de que esta función esté correctamente implementada)
            enviar_mensaje_formulario_contactar(name, email, telefono)
            enviar_confirmacion_cliente(name, email)
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')

            # Redirigir a la página de contacto
            return redirect('arigato')

        except Exception as e:
            # Si hay algún error al enviar el mensaje, redirigir a error404
            return redirect('error404')

    # Si el método no es POST, simplemente renderizar la página de contacto
    return render(request, 'pagarigato.html')


def enviar_mensaje_contacto_web_desing_senpai(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        # Verificar si todos los campos están completos
        if not name or not email or not telefono:
            # Si algún campo está vacío, redirigir a error404
            return redirect('error404')

        try:
            # Llamar a la función para enviar el mensaje (asegúrate de que esta función esté correctamente implementada)
            enviar_mensaje_formulario_contactar_web_senpai(name, email, telefono)
            enviar_confirmacion_cliente(name, email)
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')

            # Redirigir a la página de contacto
            return redirect('arigato')

        except Exception as e:
            # Si hay algún error al enviar el mensaje, redirigir a error404
            return redirect('error404')

    # Si el método no es POST, simplemente renderizar la página de contacto
    return render(request, 'pagarigato.html')


def enviar_mensaje_contacto_web_desing_kaiju(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        # Verificar si todos los campos están completos
        if not name or not email or not telefono:
            # Si algún campo está vacío, redirigir a error404
            return redirect('error404')

        try:
            # Llamar a la función para enviar el mensaje (asegúrate de que esta función esté correctamente implementada)
            enviar_mensaje_formulario_contactar_web_kaiju(name, email, telefono)
            enviar_confirmacion_cliente(name, email)
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')

            # Redirigir a la página de contacto
            return redirect('arigato')

        except Exception as e:
            # Si hay algún error al enviar el mensaje, redirigir a error404
            return redirect('error404')

    # Si el método no es POST, simplemente renderizar la página de contacto
    return render(request, 'pagarigato.html')


def enviar_mensaje_contacto_server_owncloud(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        paquete = request.POST.get('paquete')

        # Verificar si todos los campos están completos
        if not name or not email or not telefono:
            # Si algún campo está vacío, redirigir a error404
            return redirect('error404')

        try:
            # Llamar a la función para enviar el mensaje (asegúrate de que esta función esté correctamente implementada)
            enviar_mensaje_formulario_servidores_owncloud(name, email, telefono, paquete)
            # Enviar confirmación al cliente
            enviar_confirmacion_cliente(name, email)
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')

            # Redirigir a la página de contacto
            return redirect('arigato')

        except Exception as e:
            # Si hay algún error al enviar el mensaje, redirigir a error404
            return redirect('error404')

    # Si el método no es POST, simplemente renderizar la página de contacto
    return render(request, 'pagarigato.html')


def enviar_mensaje_devs(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asent = request.POST.get('asent')
        proyect = request.POST.get('proyect')
        message = request.POST.get('message')
        tipo_proyecto = request.POST.get('tipo_proyecto')
        plazo_entrega = request.POST.get('plazo_entrega')
        expectativas = request.POST.get('expectativas')

        # Verificar si todos los campos están completos
        if not name or not email or not telefono or not asent or not proyect or not message:
            # Si algún campo está vacío, redirigir a error404
            return redirect('error404')

        try:
            # Llamar a la función para enviar el mensaje (asegúrate de que esta función esté correctamente implementada)
            enviar_mensaje_formulario_devs(name, email, telefono, asent, proyect, message, tipo_proyecto, plazo_entrega, expectativas)
            enviar_confirmacion_cliente(name, email)
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            # Si el mensaje se envió correctamente, mostrar un mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')

            # Redirigir a la página de contacto
            return redirect('arigato')

        except Exception as e:
            # Si hay algún error al enviar el mensaje, redirigir a error404
            return redirect('error404')

    # Si el método no es POST, simplemente renderizar la página de contacto
    return render(request, 'pagarigato.html')