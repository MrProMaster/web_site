from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label="Логин", required=True)
    passwd = forms.CharField(label="Логин", required=True)

