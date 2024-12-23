from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
]