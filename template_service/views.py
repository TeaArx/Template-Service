from rest_framework import viewsets
from jsonschema import validate, ValidationError
from rest_framework import status
from rest_framework.response import Response
from template_service.schemas import route_schema
from . import serializers
from template_service.models import (
    Pattern,
    ApplicationType,
)


class ApplicationTypeView(viewsets.ModelViewSet):
    """Представление Типов заявки"""

    serializer_class = serializers.ApplicationTypeSerializer
    queryset = ApplicationType.objects.all()
    pagination_class = None


class PatternView(viewsets.ModelViewSet):
    """Представление Шаблонов"""

    serializer_class = serializers.PatternSerializer
    queryset = Pattern.objects.all()
    pagination_class = None

    def create(self, request, *args, **kwargs):
        return self._validate_and_process(request, *args, **kwargs, method="create")

    def update(self, request, *args, **kwargs):
        return self._validate_and_process(request, *args, **kwargs, method="update")

    def _validate_and_process(self, request, *args, **kwargs):
        try:
            validate(instance=request.data.get("pattern"), schema=route_schema)
        except ValidationError as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
