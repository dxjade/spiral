#from django.shortcuts import render #원래있던것인데 책엔 없길레 일단 주석 처리함.181016

# Create your views here.
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'