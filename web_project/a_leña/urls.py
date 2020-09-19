from django.urls import path
from . import views

app_name='alena'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('info/', views.InfoView.as_view(), name='info'),
    path('reservas/', views.ReservasView.as_view(), name='reservas'),
    path('reservar/', views.ReservarView.as_view(), name='reservar'),
    path('reserva/<int:pk>/eliminar/', views.EliminarView.as_view(), name='eliminar'),
    path('reserva/<int:pk>/detalle', views.Mi_reservaView.as_view(), name='reserva'),
]
