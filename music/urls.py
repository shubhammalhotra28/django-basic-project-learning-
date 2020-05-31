#from django.conf.urls import url
from django.urls import path
from . import views # setting the view . -> for current directory

urlpatterns = [
	
	path('',views.index, name = 'index'), # default homepage

]

