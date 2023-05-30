from django.shortcuts import render
from flightapp.models import Flight,Passenger,Reservation
from flightapp.serializers import FlightSerializer,ReservationSerializer,PassengerSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def findflight(request):
    print(request.data["date_of_departure"])
    flights = Flight.objects.filter(departurecity =request.data['departurecity'],
                                    arrival_city=request.data[ 'arrival_city'],
                                    date_of_departure=request.data['date_of_departure']  )
    seralizer = FlightSerializer(flights,many = True)
    return Response(seralizer.data)

@api_view(['POST'])
def save_reservation(request):
   flight = Flight.objects.get(id = request.data['flightId'])
   passenger = Passenger.objects.create(firstname = request.data['firstname'],
                                        lastname = request.data['lastname'],
                                        email = request.data['email'],
                                        phone= request.data['phonenumber'])
   reservation = Reservation.objects.create(flight=flight, passenger =passenger)
   return Response(["sucess"])

   
class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()

class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

class PassengerView(viewsets.ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()


