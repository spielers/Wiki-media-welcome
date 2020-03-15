from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
	"""
	Return Message 
	"""
	return HttpResponse("Wwlcometo the Wikimedia! zulip")