from django import forms



class CursoFormulario(forms.Form):
    #especificamos los campos del formulario
    nombre= forms.CharField(max_length=50)
    comision= forms.IntegerField()
    
