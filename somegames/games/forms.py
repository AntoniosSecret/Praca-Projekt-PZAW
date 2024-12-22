from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=36,
        label='Nazwa',
        label_suffix='',
        widget=forms.TextInput,
    )

    password = forms.CharField(
        min_length=8,
        label='Hasło',
        label_suffix='',
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'id': 'usernameInput',
            'name': 'username',
            'placeholder': 'Nazwa tutaj....',
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-input',
            'id': 'passwordInput',
            'name': 'password',
            'placeholder': 'Hasło tutaj....',
        })