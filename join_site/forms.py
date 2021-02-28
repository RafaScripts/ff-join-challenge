from django import forms
from .models import Target


class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ('name', 'latitude', 'longitude', 'expiration_date')
        labels = {
            'name': 'Nome',
            'expiration_date': 'Data de Expiração'
        }
        widgets = {
            'expiration_date': forms.SelectDateWidget()
        }
