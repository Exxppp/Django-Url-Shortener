from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Username", 'id': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Password", 'id': 'Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Your First Name", 'id': 'FirstName'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Your Last Name", 'id': 'LastName'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Username", 'id': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Your Email", 'id': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Password", 'id': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Repeat your password", 'id': 'RepeatPassword'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                                 required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), required=False)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
