from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Request, Driver
import os
import csv
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.core import serializers


# Create a client
class RequestView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        jd = json.loads(request.body)
        print(jd)
        print(jd['driver'])
        driver=jd['driver']
        driverOBJ=Driver.objects.create(id=driver['id'],lat=driver['lat'],lng=driver['lng'])
        Request.objects.create(idRequest=jd['idRequest'],latPickUp=jd['lat'], lngpickup=jd['lng'],driver=driverOBJ)
        datos = {'message': "book successful"}
        return JsonResponse(datos)

    # Retrieve client list
    def get(self,request):

        Request_json = serializers.serialize("json", Request.objects.all())
        requests = list(Request.objects.all())
        if len(requests) > 0:
            datos = {'message': "Success", 'requests': Request_json}
        else:
            datos = {'message': "Requests not found..."}
        
        return JsonResponse(datos)

    def get_queryset(self,request,driver):
        requests = list(Request.objects.filter(driver=driver).values())
        return JsonResponse(requests)    

class DriverView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self,lat, long):
        driver = Request.objects.get(lat__iexact=lat,long__iexact=long)
        return JsonResponse(driver)



