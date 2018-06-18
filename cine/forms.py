from django import forms

class CineForm(forms.Form):
    titulo = forms.CharField(label = "", max_length = 50, widget = forms.TextInput(attrs = {'placeholder' : 'Titulo'}))
    comentario = forms.CharField(label = "", widget = forms.Textarea(attrs={'placeholder' : 'Comentario...'}))
