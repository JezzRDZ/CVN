from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.utils import timezone
from .models import Event
from .forms import ContactForm

# Create your views here.

def events(request):
	events = Event.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'cvn/events.html', {'events': events})

def home(request):
	return render(request, 'cvn/index.html', {})

def contact(request):
	form_class = ContactForm
	if request.method == 'POST':
		form = form_class(data = request.POST)
		if form.is_valid():
			name = request.POST.get('name', '')
			phone = request.POST.get('phone', '')
			mail = request.POST.get('mail', '')
			content = request.POST.get('content', '')
			template = get_template('cvn/contact_template.txt')
			context = {
				'name': name,
				'phone': phone,
				'mail': mail,
				'content': content,
			}
			content = template.render(context)
			mail = EmailMessage(
				"Nueva solicitud de contacto",
				content,
				"Your website" +'',
				['jez.rdz95@gmail.com'],
				headers = {'Reply to': mail}
			)
			email.send()
			return redirect('contact')
	return render(request, 'cvn/contact.html', {'form': form_class})