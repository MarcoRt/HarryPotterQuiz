from django.urls import path
from . import views
from .views import (HomePageView,QuizPageView)
urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('index/',HomePageView.as_view(),name='index'),
    path('quiz/',QuizPageView.as_view(),name='quiz'),
    path('resultados/',QuizPageView.as_view(),name='resultados'),
]
