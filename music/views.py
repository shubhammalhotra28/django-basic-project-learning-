#from django.shortcuts import render
from .models import Album
from django.template import loader
# Create your views here.

# take a req and send http response

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	all_albums = Album.objects.all()
	# templates = loader.get_template('music/index.html')
	context = {
		'all_albums': all_albums,
	}
	# return HttpResponse(templates.render(context,request))
	return render(request, 'music/index.html', context= context)
	#return HttpResponse(""<h1> this is the music app homepage </h1>)

def detail(request, album_id):
	return HttpResponse("<h2> Details for album id : </h2>"+ str(album_id))

