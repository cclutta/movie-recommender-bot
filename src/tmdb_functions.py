#!/usr/bin/python3
""" TMDB Functions module."""
import requests
import json

tmdb_url = "https://api.themoviedb.org/3"
api_key = "2e0d5485fe59596911c9670fc3d70f9a"

def top_rated_request(page_no):
    """ send request to get top-rated. """
    return requests.get(
        tmdb_url+"/movie/top_rated",
        params={'api_key':api_key, 'page':page_no}     
    ).json()

def get_all_movie_genres_request():
    """ Get official movie genre list. """
    
    return requests.get(
        tmdb_url+"/genre/movie/list",
        params={'api_key':api_key}     
    ).json()

def get_top_rated_titles(page_no):
    """ Get top rated movies from TMDB. """
    top_rated = top_rated_request(page_no)
    top_rated_titles = []
        
    for result in top_rated.get("results"):
        if result.get("original_language") == "en":
            top_rated_titles.append(result.get("original_title"))
    return top_rated_titles

def get_top_rated_genreids(page_no):
    """ Get top rated movies from TMDB. """
    top_rated = top_rated_request(page_no)
    top_rated_genreids = []
        
    for result in top_rated.get("results"):
        if result.get("original_language") == "en":
            top_rated_genreids.append(result.get("genre_ids"))
    return top_rated_genreids

def get_now_playing():
    """Get movies playing now in the region. """
    
    now_playing = requests.get(
        tmdb_url+"/movie/now_playing",
        params={'api_key':api_key, 'page':1}     
    ).json()
    
    now_playing_titles = []
    
    for result in now_playing.get("results"):
        if result.get("original_language") == "en":
            now_playing_titles.append(result.get("original_title"))
    return now_playing_titles
    

  

def get_top5_based_genre(genre):
    """ Get top 5 movies based on genre. """
    pages = 10
    top_rated_titles = []
    
    for i in range(pages):
        top_rated_titles.append(get_top_rated_titles(i))
    
    top_rated_genre_titles = {}
    print(get_top_rated_titles(1))
    
   
        
if __name__ == "__main__":
    """ Main Function """
    get_top5_based_genre("cheese")
    # print(movies)
    """
    genres = get_all_movie_genres_request()
    for result in genres.get("genres"):
        print(result.get("name"))
    """
    
    
    
