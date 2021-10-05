from django import forms

class URLForm(forms.Form):
    """ To Input the Youtube URL as a form"""
    url = forms.CharField(label="Youtube URL")