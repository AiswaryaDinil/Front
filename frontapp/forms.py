from django import forms
from frontapp.models import*

class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class CreateUserForm(forms.ModelForm):
    class Meta:
        model=Useradd
        fields=["email","password","accounts","hr","sales","purchase","reports"]
        widgets={
            "email":forms.EmailInput(),
            "password":forms.PasswordInput(),
            "accounts":forms.CheckboxInput(),
            "hr":forms.CheckboxInput(),
            "sales":forms.CheckboxInput(),
            "purchase":forms.CheckboxInput(),
            "reports":forms.CheckboxInput()
        }
