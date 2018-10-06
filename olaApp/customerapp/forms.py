from django import forms


class RequestAddForm(forms.Form):
	customer_id = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'SET ID', 'required':True}))