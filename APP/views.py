from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def infopage(request):
    return render(request, 'informacion.html')


def contact(request):
    return render(request, 'contacto.html')


def services(request):
    return render(request, 'servicios.html')


def desingweb(request):
    return render(request, 'disenioweb.html')


def developersoftware(request):
    return render(request, 'desarrollosoftare.html')


def owncloudservers(request):
    return render(request, 'owncloudservers.html')


def owncloudinfor(request):
    return render(request, 'owncloudinfo.html')


def pageerror404(request):
    return render(request, '404.html')


def mensajes_view(request):
    return render(request, 'mensajes.html')


def page_error_404(request, exception):
    return render(request, '404.html', status=404)