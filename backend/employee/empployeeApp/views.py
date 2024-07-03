
from xml.dom import NotFoundErr
from django.db import transaction
from rest_framework import viewsets
from .models import Employee
# from rest_framework.response import Response
from .serializer import EmployeeSerializer

class index(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
   
    