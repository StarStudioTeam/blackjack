from card import Card, ascii_version_of_card, ascii_version_of_hidden_card
import random

class Game:
    def _start_game(self):
        suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        card_valve = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        randomSuitsName = random.choice(suits_name)
        randomValveCard = random.choice(card_valve)

        hiddenCard = Card(randomSuitsName, randomValveCard)
        showenCard = Card(randomSuitsName, randomValveCard)

        print("Bots: \n" + ascii_version_of_hidden_card(hiddenCard, showenCard))
        