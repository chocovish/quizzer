from django import forms

text = forms.TextInput(attrs={'class':'button is-info'})

class addForm(forms.Form):
    question = forms.CharField(max_length=160,widget=text)
    choice = forms.CharField(max_length=200)
    answer = forms.CharField(max_length=50)
