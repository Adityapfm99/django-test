import json
from django.core.management.base import BaseCommand
from movie.load_movies import Movie

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('movies.json') as f:
            movies = json.load(f)
            for movie in movies:
                Movie.objects.create(**movie)

                
                