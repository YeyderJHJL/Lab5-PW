from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.db.models import Count
from django.views import generic
from .models import * # Book, Author, BookInstance, Genre, Language

# Create your views here.

def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()# The 'all()' is implied by default.

    # Count genres
    num_genres = Genre.objects.annotate(num_books=Count('book')).count()
    search_word = 'Harry'  # Replace 'example' with the word you want to search for
    num_books_with_word = Book.objects.filter(title__icontains=search_word).count()



    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_word': num_books_with_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book # consulta de BBDD Book
    context_object_name = 'book_list' # Nombre identificador para plantilla
    queryset = Book.objects.filter(title__icontains='was')[:5]
    template_name = 'catalog/bookList.html'

    def get_queryset(self):
        return Book.objects.filter(title__icontains='was')[:5]
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs) # llama a BBDD
        context['algo'] = 'agregando' # crea nuevo dato y agrega
        return context
    
class BookDetailView(generic.DetailView):
    model = Book
