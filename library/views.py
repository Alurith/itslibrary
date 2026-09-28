from django.views import generic
from django.views.generic.detail import DetailView
from .models import Author, Book, Reservation
from .forms import ReservationForm

from django.urls import reverse_lazy
# Create your views here.


class IndexView(generic.ListView):
    template_name = "library/index.html"
    model = Book

    def get_queryset(self):
        qs = Book.objects.prefetch_related("authors").all()
        return qs


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book.html"


class AddReservationView(generic.CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "library/reserve_book.html"
    success_url = reverse_lazy("library:index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book_id = self.kwargs["pk"]
        return super().form_valid(form)


class CreateAuthorView(generic.CreateView):
    model = Author
    template_name = "library/generic_form.html"
    success_url = reverse_lazy("library:index")
    fields = ("full_name", "dob", "dod")


class CreateBookView(generic.CreateView):
    model = Book
    template_name = "library/generic_form.html"
    success_url = reverse_lazy("library:index")
    fields = ("title", "description", "genere", "pub_date", "authors")
