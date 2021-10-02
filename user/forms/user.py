from django import forms
from django.db.models import fields
from django.forms.widgets import TextInput
from user.models import User


class Userform(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
