import random

class random_cards:
    #this class will hold the hole cards that will get randomly generated
    def __init__(self,numbers,suits):
        self.numbers=numbers
        self.suits=suits
        self.card1=[]
        self.card2=[]
    def card(self):
        self.card1=[]
        self.card2=[]
        while self.card1==self.card2: #i will find a bettwr way later, makes sure that there is no duplicates

            self.card1=[(random.choice(self.numbers)),(random.choice(self.suits))]
            self.card2=[(random.choice(self.numbers)),(random.choice(self.suits))]







