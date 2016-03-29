from .models import Mapper
from rest_framework import viewsets
from .serializers import MapperSerializer


class MapperViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mapper.objects.all()
    serializer_class = MapperSerializer
