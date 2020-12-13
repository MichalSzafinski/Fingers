from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password1"
            }
        )
    )
    password2 = forms.CharField(
        label='Powtórz hasło',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password2"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Wybierz inna nazwę")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Ktoś już się zarejestrował z tego maila")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Błąd nazwy użytkownika")
        if qs.count() != 1:
            raise forms.ValidationError("Błąd nazwy użytkownika")
        return username
