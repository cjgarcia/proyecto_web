from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .form import reservaform
from .models import Reserva
from django.urls import reverse_lazy


# Create your views here.

class IndexView(View):
   def get(self, request):
      return render(request, 'a_leña/index.html')

class InfoView(View):
   def get(self, request):
      return render(request, 'a_leña/info.html')

class EliminarView(DeleteView):
   pass

class ReservasView(generic.ListView):
    template_name = 'a_leña/reservas_list.html'
    context_object_name = 'reservas_list'

    def get_queryset(self):
        return Reserva.objects.all()

class ReservarView(CreateView):
    model = Reserva
    fields = '__all__'
    success_url = reverse_lazy('alena:reservas')
 
class Mi_reservaView(generic.DetailView):
   model = Reserva
   fields = '__all__'
   template_name = 'a_leña/mi_reserva.html'