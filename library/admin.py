from django.contrib import admin
from .models import Book, Author

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "pub_date", "get_authors"]

    def get_authors(self, obj):
        return ", ".join([author.full_name for author in obj.authors.all()])

    get_authors.short_description = "Authors"  # Column header


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
