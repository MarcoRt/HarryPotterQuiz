from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Pregunta1, Pregunta2, Pregunta3, Pregunta4, Pregunta5, Pregunta6, Pregunta7, Pregunta8, Pregunta9, Pregunta10, Pregunta11, Pregunta12, Pregunta13, Pregunta14, Pregunta15, Pregunta16, Pregunta17, Pregunta18, Pregunta19, Pregunta20, Pregunta21, Pregunta22, Pregunta23, Pregunta24, Pregunta25, Pregunta26, Pregunta27, Pregunta28
from random import randint
# Create your views here.

def SeleccionPregunta1():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return Pregunta1()
    if(aleatorio == 2):
        return Pregunta2()
    if(aleatorio == 3):
        return Pregunta3()

def SeleccionPregunta2():
    aleatorio = randint(1,4)
    if(aleatorio == 1):
        return Pregunta15()
    if(aleatorio == 2):
        return Pregunta16()
    if(aleatorio == 3):
        return Pregunta17()
    if(aleatorio == 4):
        return Pregunta21()

def SeleccionPregunta3():
    aleatorio = randint(1,5)
    if(aleatorio == 1):
        return Pregunta13()
    if(aleatorio == 2):
        return Pregunta14()
    if(aleatorio == 3):
        return Pregunta12()
    if(aleatorio == 4):
        return Pregunta7()
    if(aleatorio == 5):
        return Pregunta9()

def SeleccionPregunta4():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return Pregunta11()
    if(aleatorio == 2):
        return Pregunta27()
    if(aleatorio == 3):
        return Pregunta28()

def SeleccionPregunta5():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return Pregunta22()
    if(aleatorio == 2):
        return Pregunta25()
    if(aleatorio == 3):
        return Pregunta26()

def SeleccionPregunta6():
    aleatorio = randint(1,6)
    if(aleatorio == 1):
        return Pregunta8()
    if(aleatorio == 2):
        return Pregunta10()
    if(aleatorio == 3):
        return Pregunta18()
    if(aleatorio == 4):
        return Pregunta19()
    if(aleatorio == 5):
        return Pregunta23()
    if(aleatorio == 6):
        return Pregunta24()

def SeleccionPregunta8():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return Pregunta4()
    if(aleatorio == 2):
        return Pregunta5()
    if(aleatorio == 3):
        return Pregunta6()
def Porcentaje_Pregunta1(respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    print("SOY LA RESPUESTA: ",type(respuesta))
    if(respuesta=='1'):
        print("LARCAMON")
        Gryffindor = 73
        Ravenclaw = 73
        Hufflepuff = 30
        Slytherin = 26
    if(respuesta=='2'):
        print("LARCAMON 2")
        Gryffindor = 27
        Ravenclaw = 27
        Hufflepuff = 70
        Slytherin = 74
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta2(respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    print("SOY LA RESPUESTA: ",type(respuesta))
    if(respuesta=='1'):
        print("LARCAMON")
        Gryffindor = 73
        Ravenclaw = 73
        Hufflepuff = 30
        Slytherin = 26
    if(respuesta=='2'):
        print("LARCAMON 2")
        Gryffindor = 27
        Ravenclaw = 27
        Hufflepuff = 70
        Slytherin = 74
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def SeleccionDeCasa(respuestas):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = Porcentaje_Pregunta1(respuestas[0])
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin += Porcentaje_Pregunta2(respuestas[0])
    print(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
def Formulario(request):
    context = {}
    form = Pregunta20(request.POST or None)
    context["casa"] = False
    context['Pregunta_1'] = SeleccionPregunta1()
    context['Pregunta_2'] = SeleccionPregunta2()
    context['Pregunta_3'] = SeleccionPregunta3()
    context['Pregunta_4'] = SeleccionPregunta4()
    context['Pregunta_5'] = SeleccionPregunta5()
    context['Pregunta_6'] = SeleccionPregunta6()
    context['Pregunta_7'] = Pregunta20()
    context['Pregunta_8'] = SeleccionPregunta8()
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("formulario")
            context = {}
            SeleccionDeCasa(temp)
            context["casa"] = "Casa marco"
    return render(request, "quiz.html", context)
class HomePageView(TemplateView):
    template_name = "index.html"
#class QuizPageView(TemplateView):
#    template_name = "quiz.html"
