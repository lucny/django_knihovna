from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    # Modul výpůjček (úkoly D–G).
    path('loans/', views.loans_list, name='loans_list'),
    path('loans/<int:pk>/', views.loan_detail, name='loan_detail'),
    # Přehled čtenářů odvozený z výpůjček (bez samostatného modelu čtenáře).
    path('readers/', views.readers_list, name='readers_list'),
    path('readers/<slug:reader_slug>/', views.reader_detail, name='reader_detail'),
]
