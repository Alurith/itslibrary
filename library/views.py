from django.views import generic
from django.views.generic.detail import DetailView
from .models import Book
# Create your views here.


class IndexView(generic.ListView):
    template_name = "library/index.html"
    model = Book

    # def get_queryset(self):
    #   qs = Book.objects.all()
    #   qs = qs.filter(genere="DB")
    #   return qs


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book.html"
