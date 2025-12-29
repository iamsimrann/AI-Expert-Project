from unittest.mock import patch
import importlib

# Import the chatbot module
bot = importlib.import_module('L1A3RulechatBot')

# Simulated inputs: name, ask for recommendation, choose beaches, say yes, ask for joke, then exit
inputs = iter(["Tester", "recommend", "beaches", "yes", "joke", "exit"])

with patch('builtins.input', lambda prompt='': next(inputs)):
    bot.chat()
