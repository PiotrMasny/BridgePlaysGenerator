class Card:
    def __init__(self, rank: str, suit: str, priority: int):
        self.rank = rank
        self.suit = suit
        self.priority = priority

    def __repr__(self) -> str:
        return f'{self.rank}{self.suit}{self.priority}'
