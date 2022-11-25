#!/usr/bin/python3

from models import storage
from models.user import User
from bot_functions import *
from chatter_bot_prototype import movie_bot

def test_add_rating():
    movie_name = read_fave_movie()
    movie_id = get_movieId_from_title(movie_name)
    
    user_email = input("Enter email address: ")
    
    if get_user_by_email(user_email) is None:
        print("No such user")
    else:
        user_id = get_user_by_email(user_email).user_id
    
    rating = input("Enter the rating: ")
    
    add_rating(user_id, movie_id, rating)
    

def test_bot():
    while True:
        try:
            bot_input = movie_bot.get_response(input())
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break
            
if __name__ == "__main__":
    """ Main Function """
    # test_add_rating()
    # print(get_movieId_from_title(read_fave_movie()))
    test_bot()
    
