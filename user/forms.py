from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control',
             'id': 'form3Example3c',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control',
             'id': 'form3Example3c',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control',
             'id': 'form3Example3c',
             }
        )

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control',
             'id': 'form3Example3c',
            }
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control',
             'id': 'form3Example3c',
            }
        )
