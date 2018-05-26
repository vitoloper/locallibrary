from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


# Book inline view
class BookInline(admin.TabularInline):
    model = Book
    extra = 0


# BookInstance inline view
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Define the Admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    inlines = (BookInline,)


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = (BookInstanceInline,)

    def display_genre(self, obj):
        """
        Creates a string for the Genre.
        """
        return ', '.join([genre.name for genre in obj.genre.all()[:3]])
    display_genre.short_description = 'Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_book_title', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

    def display_book_title(self, obj):
        """
        Display book title
        """
        return obj.book.title
    display_book_title.short_description = 'Title'
