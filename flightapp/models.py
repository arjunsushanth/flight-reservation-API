from django.db import models

class Flight(models.Model):
    flightnumber = models.CharField(max_length=10,null=True)
    departurecity = models.CharField(max_length=300,null=True)
    operating_airlines = models.CharField(max_length=300)
    arrival_city = models.CharField(max_length=300,null=True)
    date_of_departure = models.DateField()
    departure_time = models.TimeField()

class Passenger(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)   
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)  

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE) 
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)
    

# Create your models here.
