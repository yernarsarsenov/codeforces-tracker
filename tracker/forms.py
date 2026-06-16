from django import forms

class HandleForm(forms.Form):
    handle = forms.CharField(
        label='Codeforces Handle',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter your handle (e.g. tourist)',
            'autofocus': True
        })
    )
