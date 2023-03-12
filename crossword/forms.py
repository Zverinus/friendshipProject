from django import forms


class CrosswordCreationForm(forms.Form):
    word = forms.CharField(label="word1", max_length=25)

