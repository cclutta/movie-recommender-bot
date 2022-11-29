#!/usr/bin/python3

from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import asyncio
import aiohttp
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from tmdb_functions2 import *

class TMDBUpcomingSourceAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


        self.input_text = kwargs.get('input_text')

        output_text = kwargs.get('output_text')
        self.response_statement = Statement(text=output_text)

    def can_process(self, statement):
        words = ['upcoming', 'get', 'movies']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        result = get_upcoming()
        
        if len(result) > 20:
            self.response_statement.confidence = 1
        else:
            self.response_statement.confidence = 0
        
        self.response_statement.text = result
        
        return self.response_statement
