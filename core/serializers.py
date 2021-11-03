# from django.db.models import fields
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
)

from core.models import Categoria
from core.models import Fabricante
from core.models import Produto
from core.models import Compra
from core.models import ItensCompra


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class FabricanteSerializer(ModelSerializer):
    class Meta:
        model = Fabricante
        fields = "__all__"


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class FabricanteNestedSerializer(ModelSerializer):
    class Meta:
        model = Fabricante
        fields = ("marca",)


class ProdutoDetailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.tipo")
    fabricante = FabricanteNestedSerializer()

    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade", "total")
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.produto.preco


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuatio.email")
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "status", "usuario", "itens", "total")

    def get_status(self, instance):
        return instance.get_status_display()


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        models = ItensCompra
        fields = ItensCompraSerializer("produto", "quatidade")


class CriarEditarCompraSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuatio", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

    def update(sef, instance, validated_date):
        itens = validated_date.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
        return instance
