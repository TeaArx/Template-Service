from rest_framework import serializers
from .models import ApplicationType, Pattern


class ApplicationTypeSerializer(serializers.ModelSerializer):
    """Сериализатор Сервиса"""

    class Meta:
        model = ApplicationType
        fields = "__all__"


class PatternSerializer(serializers.ModelSerializer):
    """Сериализатор Шаблона"""

    class Meta:
        model = Pattern
        fields = "__all__"
