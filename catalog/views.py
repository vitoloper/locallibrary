from django.views import generic
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

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render HTML
    return render(request, 'index.html', context={'num_books': num_books, 'num_instances': num_instances,
                                             'num_instances_available': num_instances_available,
                                             'num_authors': num_authors, 'num_visits': num_visits})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
