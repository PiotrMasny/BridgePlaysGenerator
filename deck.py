import card
import random
Card = card.Card


class Deck:
    def __init__(self):
        self.cards = [
            Card(rank='2', suit='C', priority=0),
            Card(rank='3', suit='C', priority=1),
            Card(rank='4', suit='C', priority=2),
            Card(rank='5', suit='C', priority=3),
            Card(rank='6', suit='C', priority=4),
            Card(rank='7', suit='C', priority=5),
            Card(rank='8', suit='C', priority=6),
            Card(rank='9', suit='C', priority=7),
            Card(rank='T', suit='C', priority=8),
            Card(rank='J', suit='C', priority=9),
            Card(rank='Q', suit='C', priority=10),
            Card(rank='K', suit='C', priority=11),
            Card(rank='A', suit='C', priority=12),
            Card(rank='2', suit='D', priority=0),
            Card(rank='3', suit='D', priority=1),
            Card(rank='4', suit='D', priority=2),
            Card(rank='5', suit='D', priority=3),
            Card(rank='6', suit='D', priority=4),
            Card(rank='7', suit='D', priority=5),
            Card(rank='8', suit='D', priority=6),
            Card(rank='9', suit='D', priority=7),
            Card(rank='T', suit='D', priority=8),
            Card(rank='J', suit='D', priority=9),
            Card(rank='Q', suit='D', priority=10),
            Card(rank='K', suit='D', priority=11),
            Card(rank='A', suit='D', priority=12),
            Card(rank='2', suit='H', priority=0),
            Card(rank='3', suit='H', priority=1),
            Card(rank='4', suit='H', priority=2),
            Card(rank='5', suit='H', priority=3),
            Card(rank='6', suit='H', priority=4),
            Card(rank='7', suit='H', priority=5),
            Card(rank='8', suit='H', priority=6),
            Card(rank='9', suit='H', priority=7),
            Card(rank='T', suit='H', priority=8),
            Card(rank='J', suit='H', priority=9),
            Card(rank='Q', suit='H', priority=10),
            Card(rank='K', suit='H', priority=11),
            Card(rank='A', suit='H', priority=12),
            Card(rank='2', suit='S', priority=0),
            Card(rank='3', suit='S', priority=1),
            Card(rank='4', suit='S', priority=2),
            Card(rank='5', suit='S', priority=3),
            Card(rank='6', suit='S', priority=4),
            Card(rank='7', suit='S', priority=5),
            Card(rank='8', suit='S', priority=6),
            Card(rank='9', suit='S', priority=7),
            Card(rank='T', suit='S', priority=8),
            Card(rank='J', suit='S', priority=9),
            Card(rank='Q', suit='S', priority=10),
            Card(rank='K', suit='S', priority=11),
            Card(rank='A', suit='S', priority=12)
        ]

    def generate_hand(self) -> list:
        hand = random.sample(self.cards, 13)
        for one_card in hand:
            self.cards.remove(one_card)
        return self.sort_hand(hand)

    @staticmethod
    def sort_hand(hand: list):
        return sorted(hand, key=lambda one_card: (one_card.suit, one_card.priority))
