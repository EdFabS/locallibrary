from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^[0-9]{2}', views.diferente, name='diferenete'),
	url(r'^diferente/', views.diferente, name='diferenete'),
	url(r'^$', views.index, name='index'),
]