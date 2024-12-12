import card
# import random

Card = card.Card


class Player:
    # Zapisuję tu wszystkich 4 graczy
    instances = []

    def __init__(self, seat: str, hand: list, priority: int):
        self.seat = seat
        self.hand = hand
        self.priority = priority
        Player.instances.append(self)

    def __repr__(self):
        return f'{self.seat}_player'

    def __str__(self):
        return f'{self.seat}_player'

    def remove_card(self, one_card: Card):
        return self.hand.remove(one_card)

    def add_card(self, one_card: Card):
        return self.hand.append(one_card)

    # Wszystkie możliwe wisty
    def possible_first_tricks(self) -> list:
        return self.hand

    # Wszystkie możliwe dołożenia kart do wistu
    def possible_other_tricks(self, suit) -> list:
        cards_with_suit = [
            one_card for one_card in self.hand
            if one_card.suit == suit
        ]
        if not cards_with_suit:
            return self.hand
        else:
            return cards_with_suit

    # def generate_first_card(self) -> Card:
    #     one_card = random.choice(self.hand)
    #     return one_card
    #
    # def generate_card(self, suit: str) -> Card:
    #     cards_with_suit = [
    #         one_card for one_card in self.hand
    #         if one_card.suit == suit
    #     ]
    #     if not cards_with_suit:
    #         one_card = random.choice(self.hand)
    #     else:
    #         one_card = random.choice(cards_with_suit)
    #
    #     return one_card