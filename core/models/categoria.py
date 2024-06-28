from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.categoria    } {self.id}"

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = " Categorias"
