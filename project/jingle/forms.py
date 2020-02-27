from django import forms

class SongForm(forms.Form):
    song_name = forms.CharField(label='Song name', max_length=100)