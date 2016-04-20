from django import forms
from django.contrib.auth.models import User
from apps.conquers import models

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.UserProfile
        fields = ('nombre', 'last_name', 'comunity')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comunity': forms.Select(attrs={'class': 'form-control'}),
        }

class ProfileForm2(forms.ModelForm):

    class Meta:
        model = models.UserProfile
        fields = ('nombre', 'last_name')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActivityForm(forms.ModelForm):

    class Meta:
        model = models.Activity
        fields = ('name','fields')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NotaForm(forms.ModelForm):

    class Meta:
        model = models.Nota
        fields = ('name','puntuacion','comunity')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comunity': forms.Select(attrs={'class': 'form-control'}),
            'puntuacion': forms.NumberInput(attrs={'class': 'form-control'}),
        }