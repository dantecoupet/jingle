from django import forms

class SearchForm(forms.Form):
	your_name = forms.CharField(label='Song name', max_length=100)
