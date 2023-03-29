from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    author = models.CharField(db_column='author', max_length=100, blank=False)
    year = models.IntegerField(db_column='year',blank=False, default=2000)

class Usuarios(models.Model):
    email = models.CharField(db_column='email', max_length=100, blank=False)
    usuario = models.CharField(db_column='usuario', max_length=10, blank=False)
    password = models.CharField(db_column='password', max_length=10, blank=False)