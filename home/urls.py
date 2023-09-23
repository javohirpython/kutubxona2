from django.urls import path
from .views import single_book, search_book, search, book_list


urlpatterns = [
    path('books', book_list),
    path('', search_book),
    path('book/<int:pk>', single_book),
    path('search/', search),
]