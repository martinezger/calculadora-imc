from django.urls import path
from imc.views import index, mostra_personas

urlpatterns = [
    path('index/', index),
    path('personas/', mostra_personas),
]