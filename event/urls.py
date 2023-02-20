from django.urls import path

from .views import *
urlpatterns = [
    path('event/<str:name>', index),
    path('list/' , list_event),
    path('affiche/', ListEvents.as_view(), name="Affiche"),
    path('add/', AddEvent.as_view(), name="add"),

]