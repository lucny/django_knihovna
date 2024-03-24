from django.urls import path
from . import views
from .views import BookDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]
