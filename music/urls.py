#from django.conf.urls import url
from django.conf.urls import url
from django.urls import path
from . import views # setting the view . -> for current directory

app_name = 'music'

urlpatterns = [

	# /music/
	url(r'^$',views.index,name='index'),
	#path('',views.index, name = 'index'), # default homepage


	# /music/712/

	url(r'^(?P<album_id>[0-9]+)$',views.detail,name='detail'),

	# for favorite
	url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),


]

