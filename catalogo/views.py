# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
	"""
	Funación vista para la pagina inicio del sitio
	"""
	# Genera contadores de algunos de los objetos principales
	num_books=Book.objects.all().count()
	num_instances=BookInstance.objects.all().count()
	# Libros disponibles (status = 'a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count() # el 'all()' esta implicito por defecto

	#Renderiza la plantilla HTML index.html con los datos en la variable contexto
	return render(
		request,
		'index.html',
		context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
	)

def diferente(request):
	return HttpResponse("<h1>esto es como se crean las direfentes ulrs en mismas apps</h1>")

class BookListView(generic.ListView):
	model = Book

class BookDetailView(generic.DetailView):
	model = Book