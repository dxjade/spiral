from django.shortcuts import render

"""
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("Hello world")
"""
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
		model = Bookmark

class BookmarkDV(DetailView):
		model = Bookmark