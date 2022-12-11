from django import forms


class PersonForm(forms.Form):
    license = forms.CharField(label='License', max_length=32)
