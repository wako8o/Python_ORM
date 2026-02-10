import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Count, Avg
from main_app.models import Director, Actor, Movie

def populate_db():
    director_1 = Director.objects.create(
        full_name='Emil Aleksandrov',
        birth_date='1975-05-20',
        nationality='Bulgarian',
        years_of_experience=17)

    director_2 = Director.objects.create(
        full_name='Deniel Ivanov',
        birth_date='1980-03-15',
        nationality='Bulgarian',
        years_of_experience=15)

    director_3 = Director.objects.create(
        full_name='Georgi Petrov',
        birth_date='1968-11-30',
        nationality='Bulgarian',
        years_of_experience=25)

    actor_1 = Actor.objects.create(
        full_name='Ivan Ivanov',
        birth_date='1985-07-10',
        nationality='Bulgarian',
        is_awarded=True)

    actor_2 = Actor.objects.create(
        full_name='Al Pacino',
        birth_date='1940-04-25',
        nationality='American',
        is_awarded=True)

    actor_3 = Actor.objects.create(
        full_name='Robert De Niro',
        birth_date='1943-08-17',
        nationality='American',
        is_awarded=True)

    movie_1 = Movie.objects.create(
        title='The Great Adventure',
        release_date='2020-12-15',
        storyline='An epic journey of discovery and friendship.',
        genre='Action',
        rating=8.5,
        is_classic=False,
        director=director_1,
        starring_actor=actor_1
    )
    movie_1.actors.add(actor_1, actor_2)

    movie_2 = Movie.objects.create(
        title='Love in Paris',
        release_date='2019-02-14',
        storyline='A romantic tale set in the city of love.',
        genre='Comedy',
        rating=7.8,
        is_classic=False,
        director=director_2,
        starring_actor=actor_2
    )
    movie_2.actors.add(actor_2, actor_3)

    movie_3 = Movie.objects.create(
        title='The Last Stand',
        release_date='2018-10-31',
        storyline='A thrilling action movie about courage and sacrifice.',
        genre='Action',
        rating=9.0,
        is_classic=False,
        director=director_3,
        starring_actor=actor_3
    )
    movie_3.actors.add(actor_3, actor_1)

def get_directors(search_name, search_nationality):

    if search_name is None and search_nationality is None:
        return ''

    if search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(full_name__icontains=search_name,
                                            nationality__icontains=search_nationality).order_by('full_name')

    elif search_name is not None:
        directors = Director.objects.filter(full_name__icontains=search_name).order_by('full_name')

    else:
        directors = Director.objects.filter(nationality__icontains=search_nationality).order_by('full_name')

    if not directors.exists():
        return ''

    result = []
    for director in directors:
        result.append(f"Director: {director.full_name},"
                      f" nationality: {director.nationality},"
                      f" experience: {director.years_of_experience}")
    return '\n'.join(result)

def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()
    if director:
        return f"Top Director: {director.full_name}, movies: {director.num_movies}."
    return ''

def get_top_actor():
    actor = Actor.objects.prefetch_related('starring_movies')\
        .annotate(
        num_of_movies=Count('starring_movies'),
        movies_avg_rating=Avg('starring_movies__rating'))\
        .order_by('num_of_movies', 'full_name')\
        .first()

    if actor and actor.num_of_movies:
        movies = ', '.join(t.title for t in actor.starring_movies.all() if t)
        return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {movies},"
            f" movies average rating: {actor.movies_avg_rating:.1f}")

    return ''
















