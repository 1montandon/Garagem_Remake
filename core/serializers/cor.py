from rest_framework.serializers import ModelSerializer

from core.models import Cor

class CorMarSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__filds__"