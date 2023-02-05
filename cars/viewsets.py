from rest_framework import viewsets
from rest_framework.renderers import XMLRenderer

from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    renderer_classes = [XMLRenderer]
