#from django.shortcuts import render

# Create your views here.

# take a req and send http response

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return HttpResponse("<h1> this is the music app homepage </h1>")

