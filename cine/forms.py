from django import forms

class CineForm(forms.Form):
    titulo = forms.CharField(label = "Titulo ", max_length = 50)
    comentario = forms.CharField(widget = forms.Textarea)
