#!/usr/bin/python3
""" TMDB Functions module."""
import json
import asyncio
import aiohttp

tmdb_url = "https://api.themoviedb.org/3"
api_key = "2e0d5485fe59596911c9670fc3d70f9a"

async def main(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            result = await resp.json()    
    return result


def top_rated_request(page_no):
    """ send request to get top-rated. """
    return asyncio.run(main(
            tmdb_url+"/movie/top_rated", 
            params={'api_key':api_key, 'page':page_no}
            ))

def get_all_movie_genres_request():
    """ Get official movie genre list. """
    
    return asyncio.run(main(
        tmdb_url+"/genre/movie/list",
        params={'api_key':api_key}     
    ))

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
    
    now_playing = asyncio.run(main(
        tmdb_url+"/movie/now_playing",
        params={'api_key':api_key, 'page':1}     
    ))
    
    now_playing_titles = []
    
    for result in now_playing.get("results"):
        if result.get("original_language") == "en":
            now_playing_titles.append(result.get("original_title"))
    return now_playing_titles

def get_upcoming():
    """Get upcoming movies in the region. """
    
    upcoming = asyncio.run(main(
        tmdb_url+"/movie/now_playing",
        params={'api_key':api_key, 'page':1}     
    ))
    
    upcoming_titles = []
    
    for result in upcoming.get("results"):
        if result.get("original_language") == "en":
            upcoming_titles.append(result.get("original_title"))
    return upcoming_titles
    

  

def get_top5_based_genre(genre):
    """ Get top 5 movies based on genre. """
    pages = 10
    top_rated_titles = []
    top_rated_genreids = []
    top5_based_genre = []
    
    # get titles and their genre ids
    for i in range(1, pages):
        top_rated_titles.extend(get_top_rated_titles(i))
        top_rated_genreids.extend(get_top_rated_genreids(i))
    
    top_rated_genre_titles = {top_rated_titles[i]: top_rated_genreids[i] for i in   range(len(top_rated_titles))}
    
    genre_id = None
    # get specific genre id
    for result in get_all_movie_genres_request().get("genres"):
        if result.get("name").lower() == genre.lower():
            genre_id = result.get("id")
    
    for key in top_rated_genre_titles:
        if genre_id in top_rated_genre_titles[key]:
            top5_based_genre.append(key)
    
    return top5_based_genre
        
    
    
   
        
if __name__ == "__main__":
    """ Main Function """
    get_top5_based_genre("Fantasy")
    # print(movies)
    # print(asyncio.run(main(tmdb_url+"/movie/top_rated", params={'api_key':api_key, 'page':1})))
    # print(get_upcoming())
    # print(get_all_movie_genres_request())
    """
    genres = get_all_movie_genres_request()
    for result in genres.get("genres"):
        print(result.get("name"))
    """
    
    
    
