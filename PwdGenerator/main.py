#Entropy - measure of randomness / unpredictability of a password
#Entropy - log (N^L) base 2

import secrets   #for cryptographic random password generation
import string
import math  # entropy calculation

class Password:
    def __init__(self, length=12):
        self.length = length

    def generate_password(self, length):
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.specials = string.punctuation

        self.characters = self.letters + self.numbers + self.specials

        password = ''.join(secrets.choice(self.characters) for _ in range(length))
        return password

class Entropy:
    def __init__(self, password):
        self.password = password

    def calculate_entropy(self, password):
        char_pool = 0
        if any(c.islower() for c in password):
            char_pool += 26  # lowercase letters
        if any(c.isupper() for c in password):
            char_pool += 26  # uppercase letters
        if any(c.isdigit() for c in password):
            char_pool += 10  # digits 0-9
        if any(c in self.password.specials for c in password):
            char_pool += len(string.punctuation)  # special characters
        entropy = math.log2(char_pool ** len(password))

        return entropy