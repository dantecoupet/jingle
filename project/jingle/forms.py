from django import forms

class SearchForm(forms.Form):
	song = forms.CharField(label='song', max_length=100)
	
class ResultsForm(forms.Form):
	spotify_id = forms.CharField(label = 'resultsSelection', max_length = 100)
