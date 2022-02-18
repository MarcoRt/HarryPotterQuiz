from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def Hola():
    pass

class HomePageView(TemplateView):
    template_name = "index.html"
class QuizPageView(TemplateView):
    template_name = "quiz.html"
class QuizPageView(TemplateView):
    template_name = "resultados.html"
