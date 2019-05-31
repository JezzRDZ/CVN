from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class': 'form-control'}))
	phone = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class': 'form-control'}))
	mail = forms.EmailField(required = True, widget = forms.TextInput(attrs = {'class': 'form-control'}))
	content = forms.CharField(required = True, widget = forms.Textarea(attrs = {'class': 'form-control'}))
	
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Nombre'
		self.fields['phone'].label = 'Teléfono'
		self.fields['mail'].label = 'E-mail'
		self.fields['content'].label = 'Mensaje'