from django import forms

class SongForm(forms.Form):
    songTitle = forms.CharField(label="",max_length=100)