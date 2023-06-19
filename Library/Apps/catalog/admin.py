from django.contrib import admin
from .models import Book, Author, Genre, BookInstance, Language

# Register your models here.

#para introducir en BookAdmin
class BookInstanceInline(admin.TabularInline): # tambien puede ser StackedInline
    model = BookInstance

#admin.site.register(Book)
@admin.register(Book) # = adimn.site.register(Book, BookAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'display_genre')
    inlines=[BookInstanceInline]

#---------------------
class BookInlines(admin.TabularInline):
    model = Book

#admin.site.register(Author)
@admin.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields=('last_name', 'first_name', ('date_of_birth', 'date_of_death'))
    inlines=[BookInlines]


#admin.site.register(BookInstance)
@admin.register(BookInstance)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('status', 'due_back', 'id')
    list_filter=('status', 'due_back')
    fieldsets=(
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Genre)
#adicional 
admin.site.register(Language)