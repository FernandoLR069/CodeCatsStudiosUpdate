from django.urls import path
from APP import views


urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('desing-web/', views.desingweb, name='desing-web'),
    path('software-development/', views.developersoftware, name='software-development'),
    path('servers/', views.owncloudservers, name='servers'),
    path('about/', views.infopage, name='about'),
    path('contact/', views.contact, name='contact'),
    path('vermensajes_sms/', views.mensajes_view, name='messaje_send'),
    path('servers-info/', views.owncloudinfor, name='servers-info'),
    path('error404/', views.pageerror404, name='error404'),
]

# Manejador de errores 404
handler404 = views.page_error_404