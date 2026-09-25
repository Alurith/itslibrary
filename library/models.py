from django.db import models

# Create your models here.


# class Author(models.Model):
#    full_name = models.CharField(max_length=100)


class Book(models.Model):
    GENERE = {
        "DB": "Database",
        "SW": "Software",
        "HW": "Hardware",
    }
    title = models.CharField(max_length=200)
    description = models.TextField(default="descrizione del libro")
    genere = models.CharField(max_length=2, choices=GENERE)
    pub_date = models.DateTimeField("date published")
    # authors = models.ManyToManyField(Author)
