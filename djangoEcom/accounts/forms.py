from django import forms
from django.contrib.auth.models import User
from accounts.models import Address
from django.core.validators import EmailValidator


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(label='Keep me logged in', required=False)


class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            raise forms.ValidationError("Password don't match")
        return self.cleaned_data


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['address', 'address1', 'country', 'state', 'city']