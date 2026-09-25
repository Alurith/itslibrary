from django.views import generic

from .models import Book
# Create your views here.


class IndexView(generic.ListView):
    template_name = "library/index.html"
    model = Book
