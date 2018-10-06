from django import forms


class RequestAddForm(forms.Form):
	customer_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'SET ID', 'required': True}))