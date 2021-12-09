#from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets     # viewsets es otra forma de hacer un CRUD
from rest_framework.views import APIView

# trabajar con el serializador
from app1.serializers import PersonSerializer
from app1.models import Person


#----api view----#
@api_view(['GET'])
def hello(request, name):
    return Response({'message':f'Hellow world {name}'}, status = status.HTTP_200_OK)

# class ClaseUnoAPIView(APIView):
#    permission_classes = (AllowAny,)

#       def get(self, request):
#            return Response({'message':'another view'})

# visualizar los registros
#Regresa un listado de personas
class PersonListAPIView(APIView):
    #permission_classes = (AllowAny,)  #en lugar de permitir todos
    #solo van a entrar las personas auteticadas
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        #person_list = Person.objects.all()
        person_list = Person.objects.filter(status = True)
        serializer = PersonSerializer(person_list, many=True) #serializa solo un objeto
        return Response(serializer.data, status = status.HTTP_200_OK)

# crear un registro
class PersonCreateAPIView(APIView):
    #permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
       # data = request.data
        serializer = PersonSerializer(data = request.data)
        #print(serializer.is_valid())
        serializer.is_valid(raise_exception = True)
       # if not serializer.is_valid():
       #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

# Actualizar un registro
class PersonRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = (AllowAny,)

    # obtenemos id
    def get(self, request, pk):
        #try:
        #    person_obj = Person.objects,get(pk = pk)
        #except Person.DoesNotExist:
        #    return Response({'message':'No encontrado'}, status =  status.HTTP_404_NOT_FOUND) 
        person_obj = get_object_or_404(Person, pk = pk) 
        serializer = PersonSerializer(person_obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

     # actualzamos el registro
    def put(self, request, pk):
        person_obj = get_object_or_404(Person, pk = pk) 
        serializer = PersonSerializer(person_obj, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # eliminar un registro
    def delete(self, request, pk):
        person_obj = get_object_or_404(Person, pk = pk)
        person_obj.status = False # el status en false es para "eliminar" un registro
        person_obj.save()
        return Response({}, status = status.HTTP_204_NO_CONTENT)

##----- model view sets ----##
# usar view sets para catalogos y 
# las api views son para las cosas que tiene mas logica
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = Person
    permission_classes = (AllowAny,)
