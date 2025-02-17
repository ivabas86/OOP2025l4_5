from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import EmailField
from django.forms import PasswordInput, EmailInput


class TemplateForm(forms.Form):
    my_text = forms.CharField(widget=forms.Textarea)
    my_email = forms.EmailField()
    my_message = forms.CharField(widget=forms.Textarea)
