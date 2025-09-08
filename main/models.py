from django.db import models

# Create your models here.

class Curso(models.Model):
    curso_titulo = models.CharField(max_length=200)
    curso_contenido = models.TextField()
    curso_publicado = models.DateTimeField("fecha de publicacion")
    
    def __str__(self):
        return self.curso_titulo