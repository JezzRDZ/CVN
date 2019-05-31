from django.shortcuts import render
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
	return render(request, 'cvn/contact.html', {'form': form_class})