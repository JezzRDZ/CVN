from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Event
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template

def events(request):
	events = Event.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'cvn/events.html', {'events': events})

def home(request):
	return render(request, 'cvn/index.html', {})

def contact(request):
	if request.method == 'GET':
		form_class = ContactForm()
	else:
		form_class = ContactForm(request.POST)
		if form_class.is_valid():
			name = form_class.cleaned_data['name']
			phone = form_class.cleaned_data['phone']
			mail = form_class.cleaned_data['mail']
			content = form_class.cleaned_data['content']
			template = get_template('cvn/contact_template.txt')
			context = {
				'name': name,
				'phone': phone,
				'mail': mail,
				'content': content,
			}
			form_content = template.render(context)
			try:
				send_mail(name, form_content, mail, ['contacto@comunidadvidanueva.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, 'cvn/contact.html', {'form': form_class})

def success(request):
	return render(request, 'cvn/email_send.html', {})