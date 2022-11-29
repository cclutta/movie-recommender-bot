#!/usr/bin/python3

from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from classrecommender import Recommender

class RecommenderAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


        self.input_text = kwargs.get('input_text')

        output_text = kwargs.get('output_text')
        self.response_statement = Statement(text=output_text)

    def can_process(self, statement):
        if (statement.text.lower().startswith('my favorite movie is')):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        movie = input_statement.text.split("is",1)[1]
        recommender = Recommender()
        response = recommender.get_recommendations(movie, 5)
        
        if len(response) == 0:
            self.response_statement.confidence = 0
        else:
            self.response_statement.confidence = 1
        
        resp_text = "Recommendations for this movie: "
        
        for m in response:
            resp_text += ' ' + m
        
        self.response_statement.text = resp_text
        return self.response_statement
