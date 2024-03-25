from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orm/', views.orm_tester, name='orm_tester'),
]
