from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField


class Fabricante(models.Model):
    marca = models.CharField(max_length=255)

    def __str__(self):
        return self.marca


class Categoria(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    código = models.CharField(max_length=15)
    fabricante = models.ForeignKey(
        Fabricante, on_delete=models.PROTECT, related_name="Produto")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="Produto")

    def __str__(self):
        return "%s (%s)" % (self.nome, self.categoria)


class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entrgue'
    usuatio = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(
        choices=StatusCompra.choices, default=StatusCompra.CARRINHO)


class ItensCompra(models.Model):
    compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()
