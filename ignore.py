from backend.card_gen import cards
from backend.ranges import *


def initialisation():
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['s', 'd', 'c', 'h']
    h_cards = cards(numbers, suits)
    return h_cards


def start_round_txt(position, valid_range):
    init = initialisation()
    print("hello game is about to start, you will be raising first in as the " + position)
    print("score will be displayed after 10 rounds where you will have the option to continue")
    for rounds in range(1, 10):
        h_cards.card()
        card1 = whitespace(h_cards.card1)
        card2 = whitespace(h_cards.card2)
        print("cards: " + card1 + ", " + card2)
