#!/usr/bin/python3
""" Starts a Flask Web Application """

from flask import Flask, render_template
from chatbot.chatbot_prototype import movie_bot
from flask_cors import CORS
from creds import *

app = Flask(__name__)
CORS(app)

@app.route('/movie-bot-app/', strict_slashes=False)
def movie_home():
    """ Calls home """
    return render_template('index.html')

@app.route('/movie-bot-app/chat/<message>', strict_slashes=False)
def get_botresponse(message=""):
    # print(message)
    return str(movie_bot.get_response(message))

if __name__ == "__main__":
    """ Main Function """
    app.run(host=HOST, port=5000)
