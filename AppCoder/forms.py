from django import forms



class CursoFormulario(forms.Form):
    #especificamos los campos del formulario
    nombre= forms.CharField(max_length=50)
    comision= forms.IntegerField()

class ProfeFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)
    
