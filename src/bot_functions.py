#!/usr/bin/python3

from models import storage
from models.user import User
from datetime import datetime
from csv import writer
import pandas as pd
import numpy

ratings_file = "data/ratings.csv"
movies_file = "data/movies.csv"

def add_rating(user_id, movie_id, rating):
    row_list = [user_id, movie_id, rating]
    time_now = datetime.now()
    row_list.append(int(time_now.timestamp()))
    try:
        with open(ratings_file, 'a') as f:
            w_object = writer(f)
            w_object.writerow(row_list)
            f.close()
    except Exception:
       print("Error saving rating! Please try again.")

def get_user_by_email(email):
    """ Get user ID """
    uniq_u = None
    users = storage.all(User)
    for u in users:
        if u.email == email:
            uniq_u = u
    return uniq_u

def write_fave_movie(movie_name):
    try:
        with open("fave_movie.txt", 'w') as f:
            f.write(movie_name)
            f.close()
    except Exception:
       print("Error saving rating! Please try again.")

def read_fave_movie():
    fave_movie = ""
    try:
        with open("fave_movie.txt", 'r') as f:
            fave_movie = f.read()
            f.close()
    except Exception:
       print("Error saving rating! Please try again.")
    return fave_movie

def get_movieId_from_title(movie_name):
    movie_id = None
    df = pd.read_csv(movies_file)
    
    movie_id = df.loc[df['title'] == movie_name].movieId.item()
    return movie_id
    
    
    
    
    
    
    
