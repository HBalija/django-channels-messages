from django import forms
from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError

from .models import User, Message


class UserForm(forms.ModelForm):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]*$', 'This value may contain only letters, numbers and _ characters.')

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': "Username",
            'required': '',
            'autofocus': ''
        }),
        max_length=30,
        min_length=3,
        required=True,
        validators=[alphanumeric])

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': "form-control",
            'id': "email",
            'placeholder': "email@address.com",
            'required': ""
        }),
      min_length=6,
      required=True,
      validators=[validate_email])

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'placeholder': "Password",
            'required': ''
        }),
        min_length=4,
        required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            User.objects.get(email=data)
            raise ValidationError('Sorry, that email is already in use. Please login or try a different one.')
        except User.DoesNotExist:
            return data


class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': "Username",
            'required': '',
            'autofocus': ''
        }),
        required=True,)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'placeholder': "Password",
            'required': ''
        }),
        required=True)


class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control",
               'rows': "3",
               'placeholder': "",
               }),
        max_length=500,
        required=True
    )

    class Meta:
        model = Message
        fields = ('message', )
