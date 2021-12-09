# serializador

"""
puedes escribir serializadores sin relación a un modelo conserializer,
asi como serializadores reacionados a un modelo con ModelSerializer
"""

from rest_framework import serializers

#modelos que se crearon
from app1.models import Person, Job

#nombre del modelo con el que se va a trabajar y serializer
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'  #requiere todos los campos del modelo

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        models = Job
        fields = '__all__'

#serializador que no pertenece a un modelo
class MySerializer(serializers.Serializer):
    #campos del serializador
    fisrt_name = serializers.CharField(max_length = 32)
    last_name = serializers.CharField(max_length = 32)
    name = serializers.CharField(max_length = 32)
    age = serializers.IntegerField()

# puedes escribir dos seralizer para el mismo modelo
class SecondJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'name')

        