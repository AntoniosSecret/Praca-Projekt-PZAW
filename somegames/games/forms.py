from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput,
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'id': 'usernameInput',
            'placeholder': 'Nazwa tutaj....',
            'autofocus': 'True',
        })

        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['username'].label_suffix = ''

        self.fields['password'].widget.attrs.update({
            'class': 'form-input',
            'id': 'passwordInput',
            'placeholder': 'Hasło tutaj....',
        })

        self.fields['password'].label = 'Hasło'
        self.fields['password'].label_suffix = ''

class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'id': 'usernameInput',
            'placeholder': 'Nazwa tutaj....',
        })

        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['username'].label_suffix = ''
        self.fields['username'].help_text = 'Może mieć maksymalnie 150 znaków.'

        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'id': 'password1Input',
            'placeholder': 'Hasło tutaj....',
        })

        self.fields['password1'].label = 'Hasło'
        self.fields['password1'].label_suffix = ''
        self.fields['password1'].help_text = 'Musi zawierać co najmniej 8 znaków.'

        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'id': 'password2Input',
            'placeholder': 'Powtórz hasło tutaj....',
        })

        self.fields['password2'].label = 'Powtórz hasło'
        self.fields['password2'].label_suffix = ''
        self.fields['password2'].help_text = 'Wprowadź to samo hasło ponownie.'