from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.core.urlresolvers import reverse_lazy
from .models import Album
from django.views.generic import View
from .forms import UserForm
from django.urls import reverse
from django.urls import reverse_lazy



class IndexView(generic.ListView):

	template_name = 'music/index.html'
	context_object_name = 'all_albums'
	def get_queryset(self):

		return Album.objects.all()

class DetailView(generic.DetailView):

	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):


	model = Album
	fields = ['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):


	model = Album
	fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):

	model = Album
	success_url = reverse_lazy('music:index')

class UserFormView(View):

	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self,request):
		form = self.form_class(None)

		return render(request,self.template_name,{'form':form})

	# process form data

	def post(self,request):

		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

