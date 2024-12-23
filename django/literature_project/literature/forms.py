from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    author_name = forms.CharField(
        max_length=100,
        label="Автор",
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя автора'})
    )
    publication_date = forms.DateField(
        label="Дата публикации",
        input_formats=['%d.%m.%Y'],  # Укажите формат DD.MM.YYYY
        widget=forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ'})
    )

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author_name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']