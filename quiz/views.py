from django.shortcuts import render
from django.views.generic import TemplateView
from .preguntas import SeleccionPregunta1, SeleccionPregunta2, SeleccionPregunta3, SeleccionPregunta4, SeleccionPregunta5, SeleccionPregunta6, SeleccionPregunta8
from .forms import Pregunta20
from .respuestas import SeleccionDeCasa
from random import randint
# Create your views here.

#Renderiza el formulario y la respuesta
def Formulario(request):
    context = {}
    pregunta_seleccionada = [0,0,0,0,0,0,0,0]
    pregunta_seleccionada[0] = 0
    form = Pregunta20(request.POST or None)
    context["casa"] = False
    pregunta_seleccionada[0], context['Pregunta_1'] = SeleccionPregunta1()
    pregunta_seleccionada[1], context['Pregunta_2'] = SeleccionPregunta2()
    pregunta_seleccionada[2], context['Pregunta_3'] = SeleccionPregunta3()
    pregunta_seleccionada[3], context['Pregunta_4'] = SeleccionPregunta4()
    pregunta_seleccionada[4], context['Pregunta_5'] = SeleccionPregunta5()
    pregunta_seleccionada[5], context['Pregunta_6'] = SeleccionPregunta6()
    pregunta_seleccionada[6], context['Pregunta_7'] = 7 , Pregunta20()
    pregunta_seleccionada[7], context['Pregunta_8'] = SeleccionPregunta8()
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("formulario")
            context = {}
            context["casa"] = SeleccionDeCasa(pregunta_seleccionada,temp)
    return render(request, "quiz.html", context)

#Vista para presentar el index
class HomePageView(TemplateView):
    template_name = "index.html"
