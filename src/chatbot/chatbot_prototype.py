#!/usr/bin/python3

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


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

