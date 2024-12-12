import deck
import game
import player


Deck = deck.Deck
Player = player.Player
Game = game.Game


def start():
    # Tworzę cały zestaw kart
    deck1 = Deck()

    # Tworzę obiekty graczy, gdzie zostają im wylosowane karty oraz kolejność
    n_player = Player(seat='n', hand=deck1.generate_hand(), priority=0)
    e_player = Player(seat='e', hand=deck1.generate_hand(), priority=1)
    s_player = Player(seat='s', hand=deck1.generate_hand(), priority=2)
    w_player = Player(seat='w', hand=deck1.generate_hand(), priority=3)

    # Tworzę obiekt gry, gdzie określam atut oraz wistującego
    game1 = Game(trump='N', leading_player=e_player)

    # Gra się rozpoczyna
    game1.start()
