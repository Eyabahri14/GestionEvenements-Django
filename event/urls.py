from django.urls import path

from .views import *
urlpatterns = [
    path('event/<str:name>', index),
    path('list/', list_event),
    path('', ListEvents.as_view(), name="Affiche"),
    path('add/', AddEv, name="add"),
    path('update/<int:pk>', ModifierEvenement.as_view(), name="ModifierEvenement"),
    path('delete/<int:pk>', DeleteEvent.as_view(), name="deleteEvent"),
    path('details/<int:pk>', detailsss, name="details"),


]
