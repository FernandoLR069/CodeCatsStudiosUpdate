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
    path('products-info/', views.productsinfo, name='products-info'),
    path('pages-web/', views.pagesweb, name='pages-web'),
    path('servers-owncloud/', views.serverowncloud, name='servers-owncloud'),
    path('servers-owncloud-normally/', views.pagevpsbasic, name='servers-owncloud-normally'),
    path('servers-owncloud-medium/', views.pagevpsdedic, name='servers-owncloud-medium'),
    path('servers-owncloud-premium/', views.pagevpsbaremetal, name='servers-owncloud-premium'),
    path('software-development-devs/', views.devs, name='software-development-devs'),
    path('error404/', views.pageerror404, name='error404'),
    path('arigato/', views.pagearigato, name='arigato'),
]

# Manejador de errores 404
handler404 = views.page_error_404