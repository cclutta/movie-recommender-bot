#!/usr/bin/python3

from chatterbot import *
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from creds import *

movie_bot = ChatBot(
    'Jukka',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90,
        },
        {
            'import_path': 'chatbot.recommender_adapter.RecommenderAdapter'
        },
        {
            'import_path': 'chatbot.tmdb_upcomingadapter.TMDBUpcomingSourceAdapter'
        },
        {
            'import_path': 'chatbot.tmdb_nowplayingadapter.TMDBNowPlayingSourceAdapter'
        },
        {
            'import_path': 'chatbot.tmdb_ratedgenreadapter.TMDBRatedGenreAdapter'
        }
        
    ],
    database_uri=DATABASE_URI

)
trainer = ListTrainer(movie_bot)

trainer.train(
    [
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome."
])

trainer.train(
    [
    "What movie should I see?",
    "What's your favorite movie?"
    ])

