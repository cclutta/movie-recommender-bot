#!/usr/bin/python3


import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import fuzz
from bot_functions import write_fave_movie

class Recommender:
    """
    Collaborative filtering recommender using KNN
    """
    def __init__(self):
        """
        """
        self.movies_path = "data/movies.csv"
        self.ratings_path = "data/ratings.csv"
        self.model = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
        
        """ self.model.set_params(**{
            'n_neighbors': 20,
            'algorithm': 'brute',
            'metric': 'cosine'})
            """
        self.movie_r_threshold = 10
        self.user_r_threshold = 10
    
    def get_data(self):
        """
        Get and prepare data for the recommender
        """
        movies_df = pd.read_csv(
            'data/movies.csv',
            usecols=['movieId','title'],
            dtype={'movieId': 'int32', 'title': 'str'})
        # print(len(movies_df))
        ratings_df=pd.read_csv(
            'data/ratings.csv',
            usecols=['userId', 'movieId', 'rating'],
            dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
         # print(len(ratings_df))
        
        movies_count_df = pd.DataFrame(
            ratings_df.groupby('movieId').size(),
            columns=['count'])
            
        popular_movies = list(set(movies_count_df.query('count >= @self.movie_r_threshold').index))
        movies_filter = ratings_df.movieId.isin(popular_movies).values
         
        users_count_df = pd.DataFrame(
            ratings_df.groupby('userId').size(),
            columns=['count'])
        active_users = list(set(users_count_df.query('count >= @self.user_r_threshold').index))  
        users_filter = ratings_df.userId.isin(active_users).values
        
        ratings_filtered_df = ratings_df[movies_filter & users_filter]
        
        movie_user_matrix = ratings_filtered_df.pivot(
            index='movieId', columns='userId', values='rating').fillna(0)
        print(len(movie_user_matrix))
        
        hashmap = {
            movie: i for i, movie in
            enumerate(list(movies_df.set_index('movieId').loc[movie_user_matrix.index].title))
        }
               
        movie_user_sparse_matrix = csr_matrix(movie_user_matrix.values)
        
        return movie_user_sparse_matrix, hashmap
        
    def fuzzy_matching(self, hashmap, movie):
        """
        Returns match of movie provided by user.
        """
        match_tuple = []
        for title, index in hashmap.items():
            ratio = fuzz.ratio(title.lower(), movie.lower())
            if ratio >= 60:
                match_tuple.append((title, index, ratio))
        
        match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
        if not match_tuple:
            print('Oops! No match is found')
        else:
            print('Found possible matches: '
                  '{0}\n'.format([x[0] for x in match_tuple]))
            write_fave_movie(match_tuple[0][0])
            return match_tuple[0][1]

    def infer(self, model, data, hashmap, movie, no_recommendations):
        """
        Return top recommendations from movie provided by user
        """
        model.fit(data)
        idx = self.fuzzy_matching(hashmap, movie)
        distances, indices = model.kneighbors(
            data[idx],
            n_neighbors=no_recommendations+1)
        
        raw_recommendations = \
            sorted(
                list(
                    zip(
                        indices.squeeze().tolist(),
                        distances.squeeze().tolist()
                    )
                ),
                key=lambda x: x[1]
            )[:0:-1]
        return raw_recommendations
    
    def get_recommendations(self, movie, no_recommendations):
        """
        Get actual n recommendations from provided movie
        """
        movie_user_mat_sparse, hashmap = self.get_data()
        raw_recommendations = self.infer(
            self.model, movie_user_mat_sparse, hashmap,
            movie, no_recommendations) 
        reverse_hashmap = {v: k for k, v in hashmap.items()}
        list_m = []
        # print('Recommendations for {}:'.format(movie))
        for i, (idx, dist) in enumerate(raw_recommendations):
            list_m.append('{}: {} '.format(i+1, reverse_hashmap[idx]))
        return list_m

if __name__ == "__main__":
    recommender = Recommender()
    
    favorite_movie = input("Enter your fave movie: ")
    no_of_recommendations = int(input("How many movies do you want to see: "))
#     print(recommender.get_recommendations(favorite_movie, no_of_recommendations))
    


        
        
