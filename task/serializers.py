from rest_framework import serializers
from .models import members

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = members
        fields = '__all__'
        depth = 1