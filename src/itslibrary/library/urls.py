from django.urls import path

from . import views

app_name = "library"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book"),
    path("book/add", views.CreateBookView.as_view(), name="create-book"),
    path(
        "book/<int:pk>/reserve", views.AddReservationView.as_view(), name="reserve-book"
    ),
    path("author", views.CreateAuthorView.as_view(), name="create-author"),
]
