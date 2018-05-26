from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre


def index(request):
    """
    View function for index page site (home page).
    """
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Render HTML
    return render(request, 'index.html', context={'num_books': num_books, 'num_instances': num_instances,
                                             'num_instances_available': num_instances_available,
                                             'num_authors': num_authors})
