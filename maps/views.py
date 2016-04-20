from .models import Map, MapContent
from rest_framework import viewsets, generics
from .serializers import MapSerializer, MapContentSerializer

class MapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MapContent.objects.all()
    serializer_class = MapContentSerializer

class MapView(generics.ListAPIView):
    serializer_class = MapSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return Map.objects.filter(author__username=username)