from django.shortcuts import render
from .models import Event

# Create your views here.

def events(request):
	return render(request, 'cvn/events.html', {})