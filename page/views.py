from django.shortcuts import render
from django.utils import timezone
from .models import Event

# Create your views here.

def events(request):
	events = Event.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'cvn/events.html', {'events': events})