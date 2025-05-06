from django.db import models

# Create your models here.
class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bookid} - {self.name}"


class Library(models.Model):
    libid= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.libid} - {self.name}"
