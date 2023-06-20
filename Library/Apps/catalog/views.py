from django.shortcuts import render
from django.db.models import Count, Q
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
