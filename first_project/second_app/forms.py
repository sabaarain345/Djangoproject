from dataclasses import fields
from pyexpat import model
from django import forms
from second_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'