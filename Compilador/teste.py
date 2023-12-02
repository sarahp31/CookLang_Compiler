import time
import re

# Global variables
oven_temperature = 0

# Tokenizer class
class Tokenizer:
    def tokenize(self, text):
        # Simple tokenizer based on newline and space
        return [token for token in re.split(r'[ \n]', text) if token]

# Node classes
class Node:
    def evaluate(self):
        pass

class VarDec(Node):
    def __init__(self, ingredient, quantity):
        self.ingredient = ingredient
        self.quantity = quantity

    def evaluate(self):
        # Store the ingredient and its quantity
        print(f"Adding {self.quantity} of {self.ingredient}")

class PreHeatOven(Node):
    def __init__(self, temperature, time):
        self.temperature = temperature
        self.time = time

    def evaluate(self):
        global oven_temperature
        oven_temperature = self.temperature
        print(f"Pre-heating oven to {self.temperature} degrees for {self.time} seconds")
        time.sleep(self.time)

# Parser class
class Parser:
    def parse(self, tokens):
        nodes = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '@':
                ingredient = tokens[i + 1]
                quantity = tokens[i + 2]
                nodes.append(VarDec(ingredient, quantity))
                i += 3
            elif token == '%':
                command = tokens[i + 1]
                if command == 'PRE-AQUECER-FORNO':
                    temperature = int(tokens[i + 2].strip('(').rstrip(','))
                    wait_time = int(tokens[i + 3].rstrip(')'))
                    nodes.append(PreHeatOven(temperature, wait_time))
                    i += 4
            else:
                i += 1
        return nodes

# Example usage
recipe_text = """
@ farinha 2 xicara
@ acucar 1 xicara
@ manteiga 1 coler_cha

% PRE-AQUECER-FORNO(250,15)
"""

tokenizer = Tokenizer()
tokens = tokenizer.tokenize(recipe_text)

parser = Parser()
nodes = parser.parse(tokens)

for node in nodes:
    node.evaluate()
