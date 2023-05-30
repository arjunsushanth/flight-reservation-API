"""
URL configuration for flightServices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from flightapp import views

router = DefaultRouter()
router.register('flights',views.FlightViewSet,basename='flight')
router.register('passenger',views.PassengerView,basename='passenger')
router.register('reservation',views.ReservationView,basename='reservation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('findflight/',views.findflight),
    path('savereservation/',views.save_reservation),
]+router.urls
