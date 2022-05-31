from enum import auto
from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    qtdPaginas = models.IntegerField()
    isbn = models.CharField(max_length=40)
    autores = models.TextField()
    editora = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.titulo
