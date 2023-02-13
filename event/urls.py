from django.urls import path

from .views import index,list_event
urlpatterns = [
    path('event/', index),
    path('list/' , list_event)
]