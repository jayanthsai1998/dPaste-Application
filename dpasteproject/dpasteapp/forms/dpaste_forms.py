from django import forms
from django.forms import TextInput, PasswordInput, SelectDateWidget, Select, Textarea
from dpasteapp.models import *
from datetime import *
from datetime import date


class dPasteListForm(forms.ModelForm):
    class Meta:
        model = dPasteList
        exclude = ['id', 'user', 'date_created']
        widgets = {
            'project_name' : TextInput(
                attrs = {'class': 'form-control', 'placeholder': 'Project name', 'label': 'Project Name'}
            ),
            'expiry_date' : Select(
                attrs = { 'class' : 'form-control', 'label' : 'Expiry Date' }
            )
        }


class dPasteListItemForm(forms.ModelForm):
    class Meta:
        model = dPasteListItem
        exclude = ['id', 'dpastelist', ]
        widgets = {
            'syntax' : Select(
                attrs = { 'class' : 'form-control', 'label' : 'Syntax' }
            ),
            'file_name' : TextInput(
                attrs = { 'class' : 'form-control', 'placeholder' : 'File Name', 'label' : 'File Name' }
            ),
            'version' : TextInput(
                attrs = { 'class' : 'form-control', 'placeholder' : 'Eg : First Commit', 'label' : 'Version' }
            ),
            'code_snippet' : Textarea(
                attrs = { 'class': 'form-control', 'placeholder': 'Awesome Code Goes Here...', 'label': 'Code Snippet' }
            )
        }


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=75,
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First name', 'label': 'First Name'}
        )
    )
    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last name', 'label': 'Last Name'}
        )
    )
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username', 'label': 'Username'}
        )
    )
    password = forms.CharField(
        required=True,
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'label': 'Password'}
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username', 'label': 'Username'}
        )
    )
    password = forms.CharField(
        required=True,
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'label': 'Password'}
        )
    )