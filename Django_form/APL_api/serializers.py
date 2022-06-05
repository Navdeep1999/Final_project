from rest_framework import serializers
from .models import APL
class APLSerializer(serializers.ModelSerializer):
    class Meta:
        model = APL
        fields = ["task", "completed", "timestamp", "updated", "user"]