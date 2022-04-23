from django import forms
from django.core.validators import MinLengthValidator

class FormEx(forms.Form):
    name = forms.CharField(validators=[MinLengthValidator(2, "Make must be greater than 1 character")])