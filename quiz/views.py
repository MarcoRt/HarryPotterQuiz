from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Pregunta1, Pregunta2, Pregunta3, Pregunta4, Pregunta5, Pregunta6, Pregunta7, Pregunta8, Pregunta9, Pregunta10, Pregunta11, Pregunta12, Pregunta13, Pregunta14, Pregunta15, Pregunta16, Pregunta17, Pregunta18, Pregunta19, Pregunta20, Pregunta21, Pregunta22, Pregunta23, Pregunta24, Pregunta25, Pregunta26, Pregunta27, Pregunta28
from random import randint
# Create your views here.

def SeleccionPregunta1():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta1()
    if(aleatorio == 2):
        return aleatorio, Pregunta2()
    if(aleatorio == 3):
        return aleatorio, Pregunta3()

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

def SeleccionPregunta4():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta11()
    if(aleatorio == 2):
        return aleatorio, Pregunta27()
    if(aleatorio == 3):
        return aleatorio, Pregunta28()

def SeleccionPregunta5():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta22()
    if(aleatorio == 2):
        return aleatorio, Pregunta25()
    if(aleatorio == 3):
        return aleatorio, Pregunta26()

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

def SeleccionPregunta8():
    aleatorio = randint(1,3)
    if(aleatorio == 1):
        return aleatorio, Pregunta4()
    if(aleatorio == 2):
        return aleatorio, Pregunta5()
    if(aleatorio == 3):
        return aleatorio, Pregunta6()
def Porcentaje_Pregunta1(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(pregunta==1 and respuesta=='1'):
        Gryffindor = 73
        Ravenclaw = 73
        Hufflepuff = 30
        Slytherin = 26
    if(pregunta==1 and respuesta=='2'):
        Gryffindor = 27
        Ravenclaw = 27
        Hufflepuff = 70
        Slytherin = 74
    if(pregunta==2 and respuesta=='1'):
        Gryffindor = 74
        Ravenclaw = 73
        Hufflepuff = 26
        Slytherin = 28
    if(pregunta==2 and respuesta=='2'):
        Gryffindor = 26
        Ravenclaw = 27
        Hufflepuff = 74
        Slytherin = 72
    if(pregunta==3 and respuesta=='1'):
        Gryffindor = 27
        Ravenclaw = 74
        Hufflepuff = 33
        Slytherin = 72
    if(pregunta==3 and respuesta=='2'):
        Gryffindor = 73
        Ravenclaw = 26
        Hufflepuff = 67
        Slytherin = 28
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta2(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(pregunta==1 and respuesta=='1'):
        Gryffindor = 17
        Ravenclaw = 18
        Hufflepuff = 19
        Slytherin = 45
    if(pregunta==1 and respuesta=='2'):
        Gryffindor = 19
        Ravenclaw = 50
        Hufflepuff = 19
        Slytherin = 17
    if(pregunta==1 and respuesta=='3'):
        Gryffindor = 47
        Ravenclaw = 17
        Hufflepuff = 18
        Slytherin = 20
    if(pregunta==1 and respuesta=='4'):
        Gryffindor = 17
        Ravenclaw = 15
        Hufflepuff = 44
        Slytherin = 18
    if(pregunta==2 and respuesta=='1'):
        Gryffindor = 18
        Ravenclaw = 16
        Hufflepuff = 42
        Slytherin = 19
    if(pregunta==2 and respuesta=='2'):
        Gryffindor = 46
        Ravenclaw = 19
        Hufflepuff = 14
        Slytherin = 19
    if(pregunta==2 and respuesta=='3'):
        Gryffindor = 18
        Ravenclaw = 45
        Hufflepuff = 22
        Slytherin = 17
    if(pregunta==2 and respuesta=='4'):
        Gryffindor = 18
        Ravenclaw = 20
        Hufflepuff = 22
        Slytherin = 45
    if(pregunta==3 and respuesta=='1'):
        Gryffindor = 19
        Ravenclaw = 46
        Hufflepuff = 19
        Slytherin = 16
    if(pregunta==3 and respuesta=='2'):
        Gryffindor = 17
        Ravenclaw = 16
        Hufflepuff = 44
        Slytherin = 17
    if(pregunta==3 and respuesta=='3'):
        Gryffindor = 20
        Ravenclaw = 22
        Hufflepuff = 20
        Slytherin = 44
    if(pregunta==3 and respuesta=='4'):
        Gryffindor = 44
        Ravenclaw = 17
        Hufflepuff = 16
        Slytherin = 23
    if(pregunta==4 and respuesta=='1'):
        Gryffindor = 19
        Ravenclaw = 18
        Hufflepuff = 44
        Slytherin = 20
    if(pregunta==4 and respuesta=='2'):
        Gryffindor = 47
        Ravenclaw = 19
        Hufflepuff = 17
        Slytherin = 17
    if(pregunta==4 and respuesta=='3'):
        Gryffindor = 18
        Ravenclaw = 43
        Hufflepuff = 20
        Slytherin = 18
    if(pregunta==4 and respuesta=='4'):
        Gryffindor = 16
        Ravenclaw = 20
        Hufflepuff = 20
        Slytherin = 45
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta3(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(pregunta==1 and respuesta=='1'):
        Gryffindor = 21
        Ravenclaw = 44
        Hufflepuff = 19
        Slytherin = 18
    if(pregunta==1 and respuesta=='2'):
        Gryffindor = 19
        Ravenclaw = 19
        Hufflepuff = 43
        Slytherin = 20
    if(pregunta==1 and respuesta=='3'):
        Gryffindor = 41
        Ravenclaw = 18
        Hufflepuff = 19
        Slytherin = 19
    if(pregunta==1 and respuesta=='4'):
        Gryffindor = 18
        Ravenclaw = 19
        Hufflepuff = 19
        Slytherin = 43
    if(pregunta==2 and respuesta=='1'):
        Gryffindor = 17
        Ravenclaw = 20
        Hufflepuff = 20
        Slytherin = 48
    if(pregunta==2 and respuesta=='2'):
        Gryffindor = 18
        Ravenclaw = 17
        Hufflepuff = 44
        Slytherin = 18
    if(pregunta==2 and respuesta=='3'):
        Gryffindor = 21
        Ravenclaw = 46
        Hufflepuff = 19
        Slytherin = 18
    if(pregunta==2 and respuesta=='4'):
        Gryffindor = 44
        Ravenclaw = 17
        Hufflepuff = 17
        Slytherin = 16
    if(pregunta==3 and respuesta=='1'):
        Gryffindor = 17
        Ravenclaw = 45
        Hufflepuff = 18
        Slytherin = 16
    if(pregunta==3 and respuesta=='2'):
        Gryffindor = 18
        Ravenclaw = 15
        Hufflepuff = 42
        Slytherin = 17
    if(pregunta==3 and respuesta=='3'):
        Gryffindor = 16
        Ravenclaw = 22
        Hufflepuff = 21
        Slytherin = 46
    if(pregunta==3 and respuesta=='4'):
        Gryffindor = 49
        Ravenclaw = 18
        Hufflepuff = 19
        Slytherin = 21
    if(pregunta==4 and respuesta=='1'):
        Gryffindor = 14
        Ravenclaw = 18
        Hufflepuff = 46
        Slytherin = 18
    if(pregunta==4 and respuesta=='2'):
        Gryffindor = 18
        Ravenclaw = 20
        Hufflepuff = 16
        Slytherin = 46
    if(pregunta==4 and respuesta=='3'):
        Gryffindor = 19
        Ravenclaw = 44
        Hufflepuff = 21
        Slytherin = 19
    if(pregunta==4 and respuesta=='4'):
        Gryffindor = 49
        Ravenclaw = 19
        Hufflepuff = 17
        Slytherin = 17
    if(pregunta==5 and respuesta=='1'):
        Gryffindor = 44
        Ravenclaw = 17
        Hufflepuff = 16
        Slytherin = 21
    if(pregunta==5 and respuesta=='2'):
        Gryffindor = 21
        Ravenclaw = 22
        Hufflepuff = 18
        Slytherin = 46
    if(pregunta==5 and respuesta=='3'):
        Gryffindor = 16
        Ravenclaw = 45
        Hufflepuff = 22
        Slytherin = 15
    if(pregunta==5 and respuesta=='4'):
        Gryffindor = 19
        Ravenclaw = 15
        Hufflepuff = 43
        Slytherin = 18
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta4(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(pregunta==1 and respuesta=='1'):
        Gryffindor = 10
        Ravenclaw = 29
        Hufflepuff = 28
        Slytherin = 10
    if(pregunta==1 and respuesta=='2'):
        Gryffindor = 14
        Ravenclaw = 14
        Hufflepuff = 25
        Slytherin = 26
    if(pregunta==1 and respuesta=='3'):
        Gryffindor = 32
        Ravenclaw = 13
        Hufflepuff = 24
        Slytherin = 9
    if(pregunta==1 and respuesta=='4'):
        Gryffindor = 32
        Ravenclaw = 13
        Hufflepuff = 10
        Slytherin = 28
    if(pregunta==1 and respuesta=='5'):
        Gryffindor = 11
        Ravenclaw = 32
        Hufflepuff = 12
        Slytherin = 27
    if(pregunta==2 and respuesta=='1'):
        Gryffindor = 23
        Ravenclaw = 10
        Hufflepuff = 22
        Slytherin = 9
    if(pregunta==2 and respuesta=='2'):
        Gryffindor = 14
        Ravenclaw = 11
        Hufflepuff = 14
        Slytherin = 31
    if(pregunta==2 and respuesta=='3'):
        Gryffindor = 12
        Ravenclaw = 30
        Hufflepuff = 13
        Slytherin = 11
    if(pregunta==2 and respuesta=='4'):
        Gryffindor = 29
        Ravenclaw = 12
        Hufflepuff = 12
        Slytherin = 13
    if(pregunta==2 and respuesta=='5'):
        Gryffindor = 13
        Ravenclaw = 10
        Hufflepuff = 28
        Slytherin = 11
    if(pregunta==2 and respuesta=='6'):
        Gryffindor = 9
        Ravenclaw = 27
        Hufflepuff = 11
        Slytherin = 24
    if(pregunta==3 and respuesta=='1'):
        Gryffindor = 10
        Ravenclaw = 24
        Hufflepuff = 10
        Slytherin = 24
    if(pregunta==3 and respuesta=='2'):
        Gryffindor = 16
        Ravenclaw = 31
        Hufflepuff = 13
        Slytherin = 12
    if(pregunta==3 and respuesta=='3'):
        Gryffindor = 23
        Ravenclaw = 8
        Hufflepuff = 23
        Slytherin = 9
    if(pregunta==3 and respuesta=='4'):
        Gryffindor = 24
        Ravenclaw = 11
        Hufflepuff = 11
        Slytherin = 19
    if(pregunta==3 and respuesta=='5'):
        Gryffindor = 15
        Ravenclaw = 12
        Hufflepuff = 29
        Slytherin = 10
    if(pregunta==3 and respuesta=='6'):
        Gryffindor = 12
        Ravenclaw = 15
        Hufflepuff = 14
        Slytherin = 26
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta5(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(pregunta==1 and respuesta=='1'):
        Gryffindor = 10
        Ravenclaw = 22
        Hufflepuff = 10
        Slytherin = 22
    if(pregunta==1 and respuesta=='2'):
        Gryffindor = 33
        Ravenclaw = 10
        Hufflepuff = 14
        Slytherin = 13
    if(pregunta==1 and respuesta=='3'):
        Gryffindor = 13
        Ravenclaw = 9
        Hufflepuff = 26
        Slytherin = 18
    if(pregunta==1 and respuesta=='4'):
        Gryffindor = 11
        Ravenclaw = 19
        Hufflepuff = 24
        Slytherin = 9
    if(pregunta==1 and respuesta=='5'):
        Gryffindor = 18
        Ravenclaw = 13
        Hufflepuff = 13
        Slytherin = 28
    if(pregunta==1 and respuesta=='6'):
        Gryffindor = 15
        Ravenclaw = 28
        Hufflepuff = 13
        Slytherin = 10
    if(pregunta==2 and respuesta=='1'):
        Gryffindor = 19
        Ravenclaw = 6
        Hufflepuff = 9
        Slytherin = 23
    if(pregunta==2 and respuesta=='2'):
        Gryffindor = 9
        Ravenclaw = 27
        Hufflepuff = 13
        Slytherin = 12
    if(pregunta==2 and respuesta=='3'):
        Gryffindor = 19
        Ravenclaw = 7
        Hufflepuff = 18
        Slytherin = 9
    if(pregunta==2 and respuesta=='4'):
        Gryffindor = 10
        Ravenclaw = 11
        Hufflepuff = 11
        Slytherin = 28
    if(pregunta==2 and respuesta=='5'):
        Gryffindor = 9
        Ravenclaw = 9
        Hufflepuff = 27
        Slytherin = 10
    if(pregunta==2 and respuesta=='6'):
        Gryffindor = 24
        Ravenclaw = 13
        Hufflepuff = 11
        Slytherin = 9
    if(pregunta==2 and respuesta=='7'):
        Gryffindor = 11
        Ravenclaw = 27
        Hufflepuff = 11
        Slytherin = 10
    if(pregunta==3 and respuesta=='1'):
        Gryffindor = 20
        Ravenclaw = 19
        Hufflepuff = 8
        Slytherin = 8
    if(pregunta==3 and respuesta=='2'):
        Gryffindor = 10
        Ravenclaw = 23
        Hufflepuff = 9
        Slytherin = 16
    if(pregunta==3 and respuesta=='3'):
        Gryffindor = 9
        Ravenclaw = 8
        Hufflepuff = 20
        Slytherin = 20
    if(pregunta==3 and respuesta=='4'):
        Gryffindor = 24
        Ravenclaw = 23
        Hufflepuff = 8
        Slytherin = 6
    if(pregunta==3 and respuesta=='5'):
        Gryffindor = 9
        Ravenclaw = 12
        Hufflepuff = 12
        Slytherin = 26
    if(pregunta==3 and respuesta=='6'):
        Gryffindor = 22
        Ravenclaw = 8
        Hufflepuff = 20
        Slytherin = 6
    if(pregunta==3 and respuesta=='7'):
        Gryffindor = 6
        Ravenclaw = 8
        Hufflepuff = 22
        Slytherin = 19
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta6(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(pregunta==1 and respuesta=='1'):
        Gryffindor = 20
        Ravenclaw = 44
        Hufflepuff = 18
        Slytherin = 23
    if(pregunta==1 and respuesta=='2'):
        Gryffindor = 16
        Ravenclaw = 17
        Hufflepuff = 47
        Slytherin = 17
    if(pregunta==1 and respuesta=='3'):
        Gryffindor = 18
        Ravenclaw = 19
        Hufflepuff = 16
        Slytherin = 42
    if(pregunta==1 and respuesta=='4'):
        Gryffindor = 46
        Ravenclaw = 19
        Hufflepuff = 19
        Slytherin = 18
    if(pregunta==2 and respuesta=='1'):
        Gryffindor = 17
        Ravenclaw = 14
        Hufflepuff = 43
        Slytherin = 18
    if(pregunta==2 and respuesta=='2'):
        Gryffindor = 43
        Ravenclaw = 16
        Hufflepuff = 22
        Slytherin = 14
    if(pregunta==2 and respuesta=='3'):
        Gryffindor = 22
        Ravenclaw = 45
        Hufflepuff = 16
        Slytherin = 19
    if(pregunta==2 and respuesta=='4'):
        Gryffindor = 18
        Ravenclaw = 25
        Hufflepuff = 19
        Slytherin = 49
    if(pregunta==3 and respuesta=='1'):
        Gryffindor = 17
        Ravenclaw = 45
        Hufflepuff = 20
        Slytherin = 17
    if(pregunta==3 and respuesta=='2'):
        Gryffindor = 21
        Ravenclaw = 17
        Hufflepuff = 20
        Slytherin = 41
    if(pregunta==3 and respuesta=='3'):
        Gryffindor = 47
        Ravenclaw = 21
        Hufflepuff = 15
        Slytherin = 23
    if(pregunta==3 and respuesta=='4'):
        Gryffindor = 16
        Ravenclaw = 17
        Hufflepuff = 45
        Slytherin = 20
    if(pregunta==4 and respuesta=='1'):
        Gryffindor = 20
        Ravenclaw = 46
        Hufflepuff = 18
        Slytherin = 20
    if(pregunta==4 and respuesta=='2'):
        Gryffindor = 45
        Ravenclaw = 18
        Hufflepuff = 17
        Slytherin = 18
    if(pregunta==4 and respuesta=='3'):
        Gryffindor = 17
        Ravenclaw = 15
        Hufflepuff = 45
        Slytherin = 15
    if(pregunta==4 and respuesta=='4'):
        Gryffindor = 18
        Ravenclaw = 21
        Hufflepuff = 20
        Slytherin = 47
    if(pregunta==5 and respuesta=='1'):
        Gryffindor = 18
        Ravenclaw = 14
        Hufflepuff = 41
        Slytherin = 18
    if(pregunta==5 and respuesta=='2'):
        Gryffindor = 19
        Ravenclaw = 20
        Hufflepuff = 17
        Slytherin = 44
    if(pregunta==5 and respuesta=='3'):
        Gryffindor = 44
        Ravenclaw = 22
        Hufflepuff = 19
        Slytherin = 23
    if(pregunta==5 and respuesta=='4'):
        Gryffindor = 19
        Ravenclaw = 43
        Hufflepuff = 23
        Slytherin = 14
    if(pregunta==6 and respuesta=='1'):
        Gryffindor = 19
        Ravenclaw = 17
        Hufflepuff = 43
        Slytherin = 21
    if(pregunta==6 and respuesta=='2'):
        Gryffindor = 45
        Ravenclaw = 21
        Hufflepuff = 17
        Slytherin = 19
    if(pregunta==6 and respuesta=='3'):
        Gryffindor = 17
        Ravenclaw = 19
        Hufflepuff = 19
        Slytherin = 42
    if(pregunta==6 and respuesta=='4'):
        Gryffindor = 19
        Ravenclaw = 44
        Hufflepuff = 21
        Slytherin = 19
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta7(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(respuesta=='1'):
        Gryffindor = 9
        Ravenclaw = 5
        Hufflepuff = 4
        Slytherin = 8
    if(respuesta=='2'):
        Gryffindor = 7
        Ravenclaw = 5
        Hufflepuff = 5
        Slytherin = 12
    if(respuesta=='3'):
        Gryffindor = 8
        Ravenclaw = 5
        Hufflepuff = 5
        Slytherin = 11
    if(respuesta=='4'):
        Gryffindor = 6
        Ravenclaw = 5
        Hufflepuff = 5
        Slytherin = 11
    if(respuesta=='5'):
        Gryffindor = 6
        Ravenclaw = 5
        Hufflepuff = 5
        Slytherin = 10
    if(respuesta=='6'):
        Gryffindor = 6
        Ravenclaw = 11
        Hufflepuff = 5
        Slytherin = 4
    if(respuesta=='7'):
        Gryffindor = 7
        Ravenclaw = 9
        Hufflepuff = 4
        Slytherin = 4
    if(respuesta=='8'):
        Gryffindor = 7
        Ravenclaw = 11
        Hufflepuff = 5
        Slytherin = 5
    if(respuesta=='9'):
        Gryffindor = 5
        Ravenclaw = 7
        Hufflepuff = 8
        Slytherin = 5
    if(respuesta=='10'):
        Gryffindor = 6
        Ravenclaw = 11
        Hufflepuff = 5
        Slytherin = 5
    if(respuesta=='11'):
        Gryffindor = 7
        Ravenclaw = 4
        Hufflepuff = 12
        Slytherin = 4
    if(respuesta=='12'):
        Gryffindor = 6
        Ravenclaw = 5
        Hufflepuff = 11
        Slytherin = 4
    if(respuesta=='13'):
        Gryffindor = 9
        Ravenclaw = 5
        Hufflepuff = 7
        Slytherin = 5
    if(respuesta=='14'):
        Gryffindor = 6
        Ravenclaw = 4
        Hufflepuff = 11
        Slytherin = 5
    if(respuesta=='15'):
        Gryffindor = 6
        Ravenclaw = 7
        Hufflepuff = 9
        Slytherin = 5
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def Porcentaje_Pregunta8(pregunta, respuesta):
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin = 0,0,0,0
    if(pregunta==1 and respuesta=='1'):
        Gryffindor = 73
        Ravenclaw = 29
        Hufflepuff = 24
        Slytherin = 72
    if(pregunta==1 and respuesta=='2'):
        Gryffindor = 27
        Ravenclaw = 71
        Hufflepuff = 76
        Slytherin = 28
    if(pregunta==2 and respuesta=='1'):
        Gryffindor = 27
        Ravenclaw = 69
        Hufflepuff = 74
        Slytherin = 27
    if(pregunta==2 and respuesta=='2'):
        Gryffindor = 73
        Ravenclaw = 31
        Hufflepuff = 26
        Slytherin = 73
    if(pregunta==3 and respuesta=='1'):
        Gryffindor = 29
        Ravenclaw = 70
        Hufflepuff = 29
        Slytherin = 73
    if(pregunta==3 and respuesta=='2'):
        Gryffindor = 71
        Ravenclaw = 30
        Hufflepuff = 71
        Slytherin = 27
    return Gryffindor, Ravenclaw, Hufflepuff, Slytherin

def SeleccionDeCasa(pregunta, respuestas):
    Gryffindor_total, Ravenclaw_total, Hufflepuff_total, Slytherin_total = 0,0,0,0
    Gryffindor_1, Ravenclaw_1, Hufflepuff_1, Slytherin_1 = Porcentaje_Pregunta1(pregunta[0], respuestas[0])
    Gryffindor_2, Ravenclaw_2, Hufflepuff_2, Slytherin_2 = Porcentaje_Pregunta2(pregunta[1], respuestas[1])
    Gryffindor_3, Ravenclaw_3, Hufflepuff_3, Slytherin_3 = Porcentaje_Pregunta3(pregunta[2], respuestas[2])
    Gryffindor_4, Ravenclaw_4, Hufflepuff_4, Slytherin_4 = Porcentaje_Pregunta4(pregunta[3], respuestas[3])
    Gryffindor_5, Ravenclaw_5, Hufflepuff_5, Slytherin_5 = Porcentaje_Pregunta5(pregunta[4], respuestas[4])
    Gryffindor_6, Ravenclaw_6, Hufflepuff_6, Slytherin_6 = Porcentaje_Pregunta6(pregunta[5], respuestas[5])
    Gryffindor_7, Ravenclaw_7, Hufflepuff_7, Slytherin_7 = Porcentaje_Pregunta7(pregunta[6], respuestas[6])
    Gryffindor_8, Ravenclaw_8, Hufflepuff_8, Slytherin_8 = Porcentaje_Pregunta8(pregunta[7], respuestas[7])
    Gryffindor_total = Gryffindor_1 + Gryffindor_2 + Gryffindor_3 + Gryffindor_4 + Gryffindor_5 + Gryffindor_6 + Gryffindor_7 + Gryffindor_8
    Ravenclaw_total = Ravenclaw_1 + Ravenclaw_2 + Ravenclaw_3 + Ravenclaw_4 + Ravenclaw_5 + Ravenclaw_6 + Ravenclaw_7 + Ravenclaw_8
    Hufflepuff_total = Hufflepuff_1 + Hufflepuff_2 + Hufflepuff_3 + Hufflepuff_4 + Hufflepuff_5 + Hufflepuff_6 + Hufflepuff_7 + Hufflepuff_8
    Slytherin_total = Slytherin_1 + Slytherin_2 + Slytherin_3 + Slytherin_4 + Slytherin_5 + Slytherin_6 + Slytherin_7 + Slytherin_8
    lista_casas = [(Gryffindor_total,"Gryffindor"), (Ravenclaw_total, "Ravenclaw"), (Hufflepuff_total, "Hufflepuff"), (Slytherin_total,"Slytherin")]
    lista_casas.sort(reverse=True)
    casa = lista_casas[0]
    return casa[1]
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
class HomePageView(TemplateView):
    template_name = "index.html"
#class QuizPageView(TemplateView):
#    template_name = "quiz.html"
