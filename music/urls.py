#from django.conf.urls import url
from django.conf.urls import url
from django.urls import path
from . import views # setting the view . -> for current directory
from django.conf import settings
from django.conf.urls.static import static

app_name = 'music'

urlpatterns = [

	# /music/
	#url(r'^$',views.index,name='index'),
	url(r'^$',views.IndexView.as_view(),name='index'),

	#path('',views.index, name = 'index'), # default homepage


	# /music/712/

	url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),

	# for favorite
	#url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),

	# album/add/
	url(r'^album/add/$',views.AlbumCreate.as_view(),name = 'album-add'),

	# album/2/
	url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name = 'album-update'),

	# album/add/2/delete
	url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name = 'album-delete')

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

