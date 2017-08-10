from django import forms

from models import Document

class profileForm(forms.Form):
	first_name = forms.CharField(required=True, max_length=255)
	last_name = forms.CharField(required=True, max_length=255)
	email = forms.EmailField(required=True)
	phone = forms.CharField(required=True, max_length=200)
	address = forms.CharField(max_length=1000, widget=forms.Textarea())

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )