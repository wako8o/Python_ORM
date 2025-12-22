import os
import django
from django.template.defaultfilters import title

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from main_app.models import Author, Book

def show_all_authors_with_their_books():
    authors = Author.objects.all()
    result = []
    for author in authors:
        books = author.book_set.all()
        if not books:
            continue
        titles = ', '.join(x.title for x in books)
        result.append(f"{author.name} has written - {titles}!")
    return '\n'.join(result)

def delete_all_authors_without_books():
    authors = Author.objects.all()

    for author in authors:
        if author.book_set.count() == 0:
            author.delete()

