from django import forms

from short_url.models import Links


class CreateRandomUrlForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Url", 'id': 'InputUrl'
    }))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Description", 'id': 'Description'
    }))
    short_url = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': "Your short url (optional)", 'id': 'Description'
    }))

    class Meta:
        model = Links
        fields = ('url', 'description', 'short_url')
