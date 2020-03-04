from django import forms
from .models import detail

class detail_form(forms.ModelForm):
    class Meta:
        model = detail
        fields = [
            'name',
        ]