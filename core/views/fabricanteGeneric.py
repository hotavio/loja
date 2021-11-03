from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Fabricante
from core.serializers import FabricanteSerializer


class FabricantesListGeneric(ListCreateAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer


class FabricanteDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
