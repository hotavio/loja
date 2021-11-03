from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoSerializer, ProdutoDetailSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    # serializer_class = ProdutoSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoDetailSerializer
        if self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer
