from card import Card, ascii_version_of_card, ascii_version_of_hidden_card
import random

class Game:
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.deck)

    def deal_initial_cards(self):
        self.create_deck()
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]

    def calculate_hand_value(self, hand):
        total_value = sum(card.points for card in hand)
        num_aces = sum(1 for card in hand if card.rank == 'Ace')

        while total_value > 21 and num_aces:
            total_value -= 10
            num_aces -= 1

        return total_value

    def player_hit(self):
        self.player_hand.append(self.deck.pop())

    def dealer_hit(self):
        self.dealer_hand.append(self.deck.pop())

    def player_turn(self):
        while True:
            print("\nYour hand:")
            print(ascii_version_of_card(*self.player_hand))
            print("Your total:", self.calculate_hand_value(self.player_hand))

            if self.calculate_hand_value(self.player_hand) > 21:
                print("You busted!")
                return 'bust'

            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.player_hit()
            elif action == 's':
                return 'stand'
            else:
                print("Invalid input! Please enter 'h' to hit or 's' to stand.")

    def dealer_turn(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hit()

    def determine_winner(self):
        player_total = self.calculate_hand_value(self.player_hand)
        dealer_total = self.calculate_hand_value(self.dealer_hand)

        if player_total > 21:
            return "Dealer wins! Player busted."
        elif dealer_total > 21:
            return "Player wins! Dealer busted."
        elif player_total > dealer_total:
            return "Player wins!"
        elif player_total < dealer_total:
            return "Dealer wins!"
        else:
            return "It's a tie!"

    def play_game(self):
        print("Welcome to Blackjack!")
        self.deal_initial_cards()

        # Player's turn
        player_result = self.player_turn()
        if player_result == 'bust':
            print("Dealer's hand:")
            print(ascii_version_of_card(*self.dealer_hand))
            print("Dealer's total:", self.calculate_hand_value(self.dealer_hand))
            print("You lost!")
            return

        # Dealer's turn
        print("\nDealer's turn:")
        print("Dealer's hand:")
        print(ascii_version_of_hidden_card(self.dealer_hand[0], Card("Hidden", "Hidden")))
        self.dealer_turn()
        print("Dealer's hand:")
        print(ascii_version_of_card(*self.dealer_hand))
        print("Dealer's total:", self.calculate_hand_value(self.dealer_hand))

        # Determine winner
        print("\n" + self.determine_winner())