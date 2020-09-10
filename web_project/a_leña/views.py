from django.shortcuts import render
from django.views import View
from .form import reservaform
from .models import Reserva


# Create your views here.

class IndexView(View):
   def get(self, request):
      return render(request, 'a_leña/index.html')

class InfoView(View):
   def get(self, request):
      return render(request, 'a_leña/info.html')

class ResevarView(View):
   def get(self, request):
      form = reservaform(request.POST or None)
      if form.is_valid():
         form.save()
      context = {
         'form': form
      }
      return render(request, 'a_leña/reservar.html',context)
 
class Mi_reservaView(View):
   def get(self, request):
      return render(request, 'a_leña/mi_reserva.html')    
