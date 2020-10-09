from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor 
        # En esta parte defino que campos se pediran en el formulario
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre':'Nombre del autor',
            'apellidos':'Apellido del autor',
            'nacionalidad':'Nacionalidad del autor',
            'descripcion':'Pequeña descripción'
        }
        
        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor',
                    'id':'nombre'
                }
            ),
            'apellidos':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del autor',
                    'id':'apellido'
                }
            ),
            'nacionalidad':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la nacionalidad del autor',
                    'id':'nacionalidad'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una breve descripción para el autor',
                    'id':'descripcion'
                }
            ),
        }
        
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro

        fields = ['titulo','autor_id','fecha_publicacion']
        labels = {
            'titulo':'Titulo del libro',
            'autor_id':'Autor(es) del libro',
            'fecha_publicacion':'Fecha de publicación del libro',
        }

        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el titulo del libro',
                }
            ),
            'autor_id':forms.SelectMultiple(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_publicacion':forms.SelectDateWidget(),
        }
    