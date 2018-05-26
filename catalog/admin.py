from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


# Define the Admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    def display_genre(self, obj):
        """
        Creates a string for the Genre.
        """
        return ', '.join([genre.name for genre in obj.genre.all()[:3]])
    display_genre.short_description = 'Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
