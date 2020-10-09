from django.shortcuts import render, redirect
#Vistas basadas en clases
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
#Esta excepcion nos sirve para verificar cuando aplicamos el metodo ".get(id = id)"
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
from .serializers import AutorSerializer



class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = AutorSerializer
    queryset = Autor.objects.filter(estado = True)

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')


class CrearAutor(CreateView): 
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

# Eliminando solo cambiando el estado a False, Activo - Desativado
class EliminarAutor(DeleteView):
    model = Autor
    
    # No eliminarlo por completo sino que solo redifinir
    # el metodo "post"
    def post(self, request, pk, *args, **kwargs):
        autor = Autor.objects.get(id = pk)
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')

