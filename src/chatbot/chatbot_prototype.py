#!/usr/bin/python3

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from classrecommender import Recommender


movie_bot = ChatBot(
    'Jukka',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='mysql://root:root@localhost:3306/testbot'

)
trainer = ListTrainer(movie_bot)

trainer.train(
    [
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
    "What movie should I see?"
])

if __name__ == "__main__":
    recommender = Recommender()
    
    favorite_movie = input("Enter your fave movie: ")
    no_of_recommendations = int(input("How many movies do you want to see: "))
    recommender.get_recommendations(favorite_movie, no_of_recommendations)
