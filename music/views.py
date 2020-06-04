#from django.shortcuts import render
from .models import Album, Song
from django.http import Http404
from django.template import loader
# Create your views here.

# take a req and send http response

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
	all_albums = Album.objects.all()
	context = {
		'all_albums': all_albums,
	}
	return render(request,'music/index.html',context)

# to reduce try nd except
def detail(request, album_id):

	album = get_object_or_404(Album,pk=album_id)

	#try:
	#	album = Album.objects.get(pk=album_id)
	#except Album.DoesNotExist:
	#	raise Http404("Album does not exist")

	return render(request,'music/detail.html',{'album':album})


def favorite(request,album_id):

	album = get_object_or_404(Album,pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])

	except (KeyError,Song.DoesNotExist):
		return render(request,'music/detail.html',{
			'album':album,
			'error_message':"didnot selected a valid song",
		})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request,'music/detail.html',{'album':album})