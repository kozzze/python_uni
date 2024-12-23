from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Review
from .forms import BookForm, ReviewForm

def index(request):
    books = Book.objects.all()
    return render(request, 'literature/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'literature/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Получаем имя автора из формы
            author_name = form.cleaned_data['author_name']
            # Проверяем, существует ли автор в базе данных, если нет — создаем
            author, created = Author.objects.get_or_create(name=author_name)
            # Создаем книгу с привязкой к автору
            book = Book(
                title=form.cleaned_data['title'],
                publication_date=form.cleaned_data['publication_date'],
                author=author
            )
            book.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'literature/add_book.html', {'form': form})