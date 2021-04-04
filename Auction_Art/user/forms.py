from django import forms
from user.models import USER

class UserForm(forms.ModelForm):
    class Meta:
        model=USER
        fields="__all__"