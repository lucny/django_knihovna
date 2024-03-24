from django.urls import path
# Import pohledů pro zobrazení galerie autorů a detailu autora
from .views import BookDetailView, BooksListView, AuthorsListView, AuthorDetailView, index

urlpatterns = [
    # URL adresa pro zobrazení domovské stránky
    path('', index, name='index'),
    # URL adresa pro zobrazení seznamu knih
    path('books/', BooksListView.as_view(), name='books_list'),
    # URL adresa pro zobrazení detailu knihy
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    # URL adresa pro zobrazení galerie autorů
    path('authors/', AuthorsListView.as_view(), name='authors_list'),
    # URL adresa pro zobrazení detailu autora
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
]
