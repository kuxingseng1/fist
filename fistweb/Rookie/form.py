from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(label='Ypur name',max_length=100)