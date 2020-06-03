from django import forms

from recipes.models import Recipe


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'time_required',
            'instructions'
        ]
