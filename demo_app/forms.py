from django import forms
from .models import detail
from django.contrib.auth.models import User

class detail_form(forms.ModelForm):
    class Meta:
        model = detail
        fields = [
            'name',
        ]
