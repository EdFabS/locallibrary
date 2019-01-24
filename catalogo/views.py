# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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

	# Number of visits to this view, as counted in the session variable.
	num_visits=request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1

	#Renderiza la plantilla HTML index.html con los datos en la variable contexto
	return render(
		request,
		'index.html',
		context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_visits':num_visits},
	)

def diferente(request):
	return HttpResponse("<h1>esto es como se crean las direfentes ulrs en mismas apps</h1>")

class BookListView(generic.ListView):
	model = Book
	paginate_by = 2

class BookDetailView(generic.DetailView):
	model = Book
	paginate_by = 10

class AuthorListView(generic.ListView):
	model = Author

class AuthorDetailView(generic.DetailView):
	model = Author

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
	"""
	Generic class-based view listing books on loan to current user.
	"""
	model = BookInstance
	template_name ='catalog/bookinstance_list_borrowed_user.html'
	paginate_by = 10
	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')