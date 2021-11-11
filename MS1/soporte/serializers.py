from rest_framework import serializers
from .models import PQR, PersonaSoporte

class PersonaSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'

class PQRSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = PQRSerialiazer
        fields = ['PersonaSoporte','estado','comentario']
