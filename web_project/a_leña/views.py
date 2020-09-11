from django.shortcuts import render, redirect
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
      if request.method == 'POST':
         form = reservaform(request.POST or None)
         if form.is_valid():
            form.save()
            redirect('a_leña:index')
         #context = {
         # 'form': form
         #}
      else:
         form = reservaform()
      return render(request, 'a_leña/reservar.html',{'form':form})
 
class Mi_reservaView(View):
   def get(self, request):
      return render(request, 'a_leña/mi_reserva.html')    
