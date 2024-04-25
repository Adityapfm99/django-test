from django.shortcuts import render
from movie.movies import Movie
import os
import json
from django.urls import path
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator, EmptyPage

def movie_list(request):
    # Load movie data from JSON file
    json_file_path = os.path.join(os.path.dirname(__file__), 'movies.json')

    with open(json_file_path, 'r') as file:
        movies_data = json.load(file)

    # Paginate the movie data
    paginator = Paginator(movies_data, 10)  # Show 10 movies per page

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'movie/movie_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    json_file_path = os.path.join(os.path.dirname(__file__), 'movies.json')

    with open(json_file_path, 'r') as file:
        movies_data = json.load(file)
    
    movie = next((movie for movie in movies_data if movie['id'] == movie_id), None)
    
    return render(request, 'movie/movie_detail.html', {'movie': movie})
