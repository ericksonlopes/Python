from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', )
    estoque = models.IntegerField('Quantidade em estoque')
