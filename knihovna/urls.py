from django.urls import path
# Import pohledů pro zobrazení galerie autorů a detailu autora
from .views import BookDetailView, BooksListView, AuthorsListView, AuthorDetailView, index, BookCreateView, \
    BookUpdateView, BookDeleteView

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
    # URL adresa pro vložení knihy
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    # URL adresa pro aktualizaci knihy
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    # URL adresa pro smazání knihy
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
