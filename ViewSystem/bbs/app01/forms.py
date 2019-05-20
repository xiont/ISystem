from django import forms

class BBSForm(forms.Form):
    title = forms.CharField()
    summary = forms.CharField()
    content = forms.CharField()
    sign = forms.CharField()