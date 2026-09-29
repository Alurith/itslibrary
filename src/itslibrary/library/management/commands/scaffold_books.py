from datetime import date

from django.core.management.base import BaseCommand
from django.utils import timezone

from itslibrary.library.models import Author, Book


class Command(BaseCommand):
    help = "Inserisce libri e autori di esempio"

    STARTING_BOOKS = {
        "Circuiti di Nebbia": {
            "genere": "HW",
            "pub_date": timezone.now(),
            "authors": [
                {"full_name": "Ada Moretti", "dob": date(1982, 4, 10)},
            ],
        },
        "Algoritmi del Vento": {
            "genere": "SW",
            "pub_date": timezone.now(),
            "authors": [
                {"full_name": "Ada Moretti", "dob": date(1982, 4, 10)},
                {"full_name": "Bruno Serra", "dob": date(1975, 9, 22)},
            ],
        },
        "Database per Marte": {
            "genere": "DB",
            "pub_date": timezone.now(),
            "authors": [
                {"full_name": "Bruno Serra", "dob": date(1975, 9, 22)},
            ],
        },
        "Il Manuale del Pixel Perduto": {
            "genere": "HW",
            "pub_date": timezone.now(),
            "authors": [
                {"full_name": "Chiara Neri", "dob": date(1990, 1, 8)},
            ],
        },
        "Django delle Stelle": {
            "genere": "SW",
            "pub_date": timezone.now(),
            "authors": [
                {"full_name": "Chiara Neri", "dob": date(1990, 1, 8)},
                {"full_name": "Ada Moretti", "dob": date(1982, 4, 10)},
            ],
        },
    }

    def handle(self, *args, **options):
        for title, book_data in self.STARTING_BOOKS.items():
            book, created = Book.objects.get_or_create(
                title=title,
                defaults={
                    "genere": book_data["genere"],
                    "pub_date": book_data["pub_date"],
                },
            )

            for author_data in book_data["authors"]:
                author, _ = Author.objects.get_or_create(
                    full_name=author_data["full_name"],
                    defaults={"dob": author_data["dob"]},
                )
                book.authors.add(author)

            action = "inserito" if created else "già presente"
            self.stdout.write(f"Libro {action}: {book.title}")

        self.stdout.write(self.style.SUCCESS("Dati di esempio inseriti."))
