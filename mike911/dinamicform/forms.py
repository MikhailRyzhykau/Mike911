from django import forms


class InputForm(forms.Form):
    fild1 = forms.CharField(label='fild_1', max_length=30)
