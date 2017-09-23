from django import forms
from django.contrib.auth.models import User


#todo: implement a registration view
class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
