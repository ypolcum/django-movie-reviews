from django import forms
from .models import Movie

class MovieForm(forms.Form):
	movie = forms.Charfield(label='Movie name:', max_length=100)
	director = forms.Charfield(label='Director:', max_length=100)

	class Meta:
		model = Movie
		fields = ['movie', 'director']
