from django import forms

from .models import Categorie, Game
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name', 'image']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'category', 'price', 'short_text', 'image']
        widgets = {'short_text': forms.Textarea(attrs={'cols': 30, 'rows': 7})}
