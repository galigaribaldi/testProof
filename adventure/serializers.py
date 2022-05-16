from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from adventure.models import Journey
class JourneySerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()

class JourneyModelSerializer(ModelSerializer):
    class Meta:
        model = Journey
        fields = '__all__'
class JourneySerializerStop(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()
    date = serializers.DateField(input_formats=['%d-%m-%Y',])
