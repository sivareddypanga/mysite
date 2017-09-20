from django import forms
from .models import SubmitForm

class ConnectForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField(min_length=10)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5,}))

    class Meta:
        model = SubmitForm
        fields = ('name', 'email', 'mobile', 'message',)

