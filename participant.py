import random

class Participant:
    def __init__(self, salary):
        self.salary = salary
        self.noise = random.randint(1000, 10000)

    def encrypt(self):
        """Simulates encryption by adding noise."""
        return self.salary + self.noise, self.noise
