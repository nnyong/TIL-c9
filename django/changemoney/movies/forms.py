from django import forms
from .models import Movie,Score

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','audience','poster_url','description',]
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model=Score
        fields=['content','score',]