from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
import uuid  # Required for unique book instances


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Genre(models.Model):
    """
    Genre
    """
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name


class Language(models.Model):
    """
    Language
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book
    """
    title = models.CharField(max_length=200)
    # A book can only have one author. An author can have multiple books
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the book')
    imprint = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    # genre can contain many books. A book may cover many genres.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    # A book can be written in one language only.
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """

        :return: the url to access a detail record for this book.
        """
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"), )

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id, self.book.title)
