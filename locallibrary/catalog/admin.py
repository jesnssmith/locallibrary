from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
    (None, {
        'fields': ('book','imprint', 'id')
    }),
    ('Availability', {
        'fields': ('status', 'due_back','borrower')
    }),
    )

def display_genre(self):
    """
    Creates a string for the Genre. This is required to display genre in Admin.
    """
    return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
display_genre.short_description = 'Genre'



