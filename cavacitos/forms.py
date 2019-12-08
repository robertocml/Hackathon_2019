from django import forms
from .models import *


class LoginForm(forms.ModelForm):

    class Meta:
        model = Inspector
        fields = ('nombre', 'contrasena',)
