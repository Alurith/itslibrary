from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta

User = get_user_model()
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


class Reservation(models.Model):
    RESERVATION_LENGHT = {30: "30 Giorni", 60: "60 Giorni", 90: "90 Giorni"}
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField("Data Inizio Prenotazione", auto_now_add=True)
    duration = models.PositiveIntegerField(
        "Durata Prenotazione", choices=RESERVATION_LENGHT
    )

    @property
    def end_date(self):
        return self.start_date + timedelta(days=self.duration)

    def __str__(self):
        return f"{self.user.email} {self.book.title}"
