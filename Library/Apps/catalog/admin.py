from django.contrib import admin
from .models import Book, Author, Genre, BookInstance, Language

# Register your models here.

#admin.site.register(Book)
@admin.register(Book) # = adimn.site.register(Book, BokkAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'display_genre')

#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)

#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter=('status', 'due_back')

admin.site.register(Genre)
#adicional 
admin.site.register(Language)