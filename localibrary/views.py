from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    return HttpResponse("RAIZ Hello, world. You're at the catalogo index.")

def prueba(request):
	now = datetime.datetime.now()

	return HttpResponse("<h1>RAIZ esto es como se crean las direfentes ulrs en mismas apps %s</h1>" %now)
