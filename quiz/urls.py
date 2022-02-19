from django.urls import path
from . import views
from .views import (HomePageView,Formulario)
urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('index/',HomePageView.as_view(),name='index'),
    path('quiz/',Formulario,name='quiz'),
    #path('resultados/',ResultadosPageView,name='resultados'),
]
