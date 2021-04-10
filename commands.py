import subprocess
import os
import pyttsx3
from get_answer import Fetcher

engine = pyttsx3.init()


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Jarvis. How are you?")

        else:
            f = Fetcher("https://www.google.ca/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    # noinspection PyMethodMayBeStatic
    def respond(self, response):
        print(str(response))
        engine.say(str(response))
        engine.runAndWait()
