from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя автора")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    publication_date = models.DateField(verbose_name="Дата публикации")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(verbose_name="Рейтинг", choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"{self.book.title} - {self.rating} звезд"