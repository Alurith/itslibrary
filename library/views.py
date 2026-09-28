from django.views import generic
from django.views.generic.detail import DetailView
from .models import Book, Reservation
from .forms import ReservationForm

from django.urls import reverse_lazy
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


class AddReservationView(generic.CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "library/reserve_book.html"
    success_url = reverse_lazy("library:index")
