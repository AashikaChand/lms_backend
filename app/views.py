from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Department
from app.serializers import DepartmentSerializer
from lms_backend.settings import DATABASES

# Create your views here.
@api_view(['GET'])
def department(request):
    data = {
        'departments':DepartmentSerializer(Department.objects.all(),many=True).data
    }
    return Response(data)

@api_view(['GET'])
def deleteDepartment(request,givenId):
  Department.objects.get(id=givenId).delete()
  return Response({'status':200}) 

@api_view(['POST'])
def addDepartment(request):
    datas = request.data 
    Department(name = datas['departmentName']).save()
    return Response({'status':200})    
