from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from event.models import Event
from .serializer import EventSerializer


@api_view(['GET'])
def getEvents(request):
      events = Event.objects.all()
      serializer = EventSerializer(events , many=True)
      return Response(serializer.data ,status=status.HTTP_200_OK )


@api_view(['POST'])
def addEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT'])
def updateEvent(request , id= None):
    event = Event.objects.get(id=id)

    serializer = EventSerializer(instance=event,data=request.data)
    if serializer.is_valid():
            serializer.save()
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET','DELETE'])
def deleteEvent(request, id=None):
    try:
        event = Event.objects.get(id=id)
    except event.DoesNotExist:
        return Response(status="Event not found")

    event.delete()
    return Response("Event deleted")