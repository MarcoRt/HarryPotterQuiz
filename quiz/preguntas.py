from random import randint
from .forms import Pregunta1, Pregunta2, Pregunta3, Pregunta4, Pregunta5, Pregunta6, Pregunta7, Pregunta8, Pregunta9, Pregunta10, Pregunta11, Pregunta12, Pregunta13, Pregunta14, Pregunta15, Pregunta16, Pregunta17, Pregunta18, Pregunta19, Pregunta20, Pregunta21, Pregunta22, Pregunta23, Pregunta24, Pregunta25, Pregunta26, Pregunta27, Pregunta28

#Selección aleatoria para el conjunto 1 de preguntas
def SeleccionPregunta1():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta1()
    if(aleatorio == 2):
        return aleatorio, Pregunta2()
    if(aleatorio == 3):
        return aleatorio, Pregunta3()

#Selección aleatoria para el conjunto 2 de preguntas
def SeleccionPregunta2():
    aleatorio = randint(1,4)
    if(aleatorio == 1):
        return aleatorio, Pregunta15()
    if(aleatorio == 2):
        return aleatorio, Pregunta16()
    if(aleatorio == 3):
        return aleatorio, Pregunta17()
    if(aleatorio == 4):
        return aleatorio, Pregunta21()

#Selección aleatoria para el conjunto 3 de preguntas
def SeleccionPregunta3():
    aleatorio = randint(1,5)
    if(aleatorio == 1):
        return aleatorio, Pregunta13()
    if(aleatorio == 2):
        return aleatorio, Pregunta14()
    if(aleatorio == 3):
        return aleatorio, Pregunta12()
    if(aleatorio == 4):
        return aleatorio, Pregunta7()
    if(aleatorio == 5):
        return aleatorio, Pregunta9()

#Selección aleatoria para el conjunto 4 de preguntas
def SeleccionPregunta4():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta11()
    if(aleatorio == 2):
        return aleatorio, Pregunta27()
    if(aleatorio == 3):
        return aleatorio, Pregunta28()

#Selección aleatoria para el conjunto 5 de preguntas
def SeleccionPregunta5():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta22()
    if(aleatorio == 2):
        return aleatorio, Pregunta25()
    if(aleatorio == 3):
        return aleatorio, Pregunta26()

#Selección aleatoria para el conjunto 6 de preguntas
def SeleccionPregunta6():
    aleatorio = randint(1,6)
    if(aleatorio == 1):
        return aleatorio, Pregunta8()
    if(aleatorio == 2):
        return aleatorio, Pregunta10()
    if(aleatorio == 3):
        return aleatorio, Pregunta18()
    if(aleatorio == 4):
        return aleatorio, Pregunta19()
    if(aleatorio == 5):
        return aleatorio, Pregunta23()
    if(aleatorio == 6):
        return aleatorio, Pregunta24()

#Selección aleatoria para el conjunto 8 de preguntas
def SeleccionPregunta8():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta4()
    if(aleatorio == 2):
        return aleatorio, Pregunta5()
    if(aleatorio == 3):
        return aleatorio, Pregunta6()
