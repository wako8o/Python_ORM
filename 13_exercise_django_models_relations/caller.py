import os
from datetime import timedelta, date, datetime

import django
from django.db.models import Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from main_app.models import Author, Book, Song, Artist, Product, Review, Driver, DrivingLicense, Owner, Car, \
    Registration


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
        books = author.book_set.count()
        if books == 0:
            author.delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)

def get_songs_by_artist(artist_name: str):
    artists = Artist.objects.get(name=artist_name).songs.order_by('-id')
    return artists

def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    return Review.objects.filter(product__name=product_name).aggregate(avg_rating=Avg('rating'))['avg_rating']

    # product = Product.objects.get(name=product_name)
    # reviews = product.reviews.all()
    #
    # avg_score = sum(r.rating for r in reviews) / len(reviews)
    # return avg_score

def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)

def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')

def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    expiration_date = 365
    driving_license = DrivingLicense.objects.all().order_by('-license_number')
    result = []

    for license in driving_license:
        expire = license.issue_date + timedelta(days=expiration_date)
        result.append(f"License with number: {license.license_number} expires on {expire}!")
    return '\n'.join(result)

    # licenses = DrivingLicense.objects.order_by('-license_number')
    # return "\n".join(str(l) for l in licenses)

def get_drivers_with_expired_licenses(due_date: date):
    expired_licenses = DrivingLicense.objects.all()
    result = []

    for license in expired_licenses:
        expire = license.issue_date + timedelta(days=365)
        if expire < due_date:
            result.append(license.driver)
    return result

    # return Driver.objects.filter(
    #     license__issue_date__lt=due_date - timedelta(365),
    # )


def register_car_by_owner(owner: Owner):
    car = Car.objects.filter(registration__isnull=True).first()
    registration = Registration.objects.filter(car__isnull=True).first()

    car.owner = owner
    car.registration = registration

    car.save()

    registration.registration_date = datetime.today()
    registration.car = car

    registration.save()

    return (
        f"Successfully registered {car.model} to "
        f"{owner.name} with registration number "
        f"{registration.registration_number}."
    )

