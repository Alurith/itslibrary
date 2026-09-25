from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    dob = models.DateField("data di nascita")
    dod = models.DateField("data di morte", null=True, blank=True)

    def __str__(self):
        return self.full_name


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
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
