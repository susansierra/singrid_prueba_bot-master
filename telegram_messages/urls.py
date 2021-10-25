# from django.contrib import admin
from django.urls import path, include
from . import views
# from django import urls
urlpatterns = [
    path('enviar_mensaje_colectivo/', views.sendMessageToEveryOne, name="enviar_mensaje_colectivo"),
    path('enviar_mensaje/', views.sendMessage, name="enviar_mensaje"),
    path('obtener_actualizacion/', views.getUpdates, name="obtener_actualizacion")
]