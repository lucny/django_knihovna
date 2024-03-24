from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BooksListView.as_view(), name='books_list'),
]
