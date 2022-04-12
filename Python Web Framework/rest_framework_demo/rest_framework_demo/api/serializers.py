from rest_framework import serializers

from rest_framework_demo.api.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'