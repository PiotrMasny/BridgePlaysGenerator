import player


Player = player.Player


class Game:
    def __init__(self, trump: str, leading_player: Player):
        self.trump = trump
        self.leading_player = leading_player
        self.ns_tricks = 0
        self.ew_tricks = 0
        self.possible_plays = []

    def change_priority_with_trump(self):
        # Sprawdzam, czy gra jest atutowa, jeśli nie, to nie zmieniam priorytetu
        if self.trump in ['C', 'D', 'H', 'S']:
            for one_player in Player.instances:
                for card in one_player.hand.copy():
                    if card.suit == self.trump:
                        card.priority += 26

    @staticmethod
    def change_priority_without_trump(suit):
        if suit in ['C', 'D', 'H', 'S']:
            for one_player in Player.instances:
                for card in one_player.hand.copy():
                    if card.suit == suit:
                        card.priority += 13

    @staticmethod
    def back_priority(suit):
        if suit in ['C', 'D', 'H', 'S']:
            for one_player in Player.instances:
                for card in one_player.hand.copy():
                    if card.suit == suit:
                        card.priority -= 13

    def generate_plays(
            self,
            possible_plays: list,
            tricks_left: int,
            ns_tricks: int,
            ew_tricks: int,
            first_lead_player: Player
    ):
        # Warunek wyjścia z pętli, a więc w przypadku, gdy będzie 13 lew
        if tricks_left == 0:

            # Dodaję do głównego pojemnika 13 lew jako jeden z możliwych scenariuszy
            self.possible_plays.append(possible_plays.copy())

            # Opuszczam rekurencję
            return

        # 1 gracza przesyłam argumentem
        # Srawdzam, który gracz będzie odpowiednio 2, 3 i 4
        second_player_priority = (first_lead_player.priority + 1) % 4
        second_lead_player = next(
            one_player for one_player in Player.instances if
            one_player.priority == second_player_priority
        )
        third_player_priority = (second_player_priority + 1) % 4
        third_lead_player = next(
            one_player for one_player in Player.instances if
            one_player.priority == third_player_priority
        )
        forth_player_priority = (third_player_priority + 1) % 4
        forth_lead_player = next(
            one_player for one_player in Player.instances if
            one_player.priority == forth_player_priority
        )

        # Dla każdego możliwego wistu
        for first_lead in first_lead_player.possible_first_tricks().copy():
            suit_of_lead = first_lead.suit

            # Dla każdego możliwego 2 dołożenia do lewy
            for second_lead in second_lead_player.possible_other_tricks(suit_of_lead).copy():

                # Dla każdego możliwego 3 dołożenia do lewy
                for third_lead in third_lead_player.possible_other_tricks(suit_of_lead).copy():

                    # Dla każdego możliwego 4 dołożenia do lewy
                    for forth_lead in forth_lead_player.possible_other_tricks(suit_of_lead).copy():

                        # Zmieniam priorytet, podnosząc kolor wistu
                        self.change_priority_without_trump(suit_of_lead)

                        # Tworzę słownik, żeby zobaczyć, który z graczy zgarnie lewę
                        leads = {
                            first_lead_player: first_lead.priority,
                            second_lead_player: second_lead.priority,
                            third_lead_player: third_lead.priority,
                            forth_lead_player: forth_lead.priority
                        }

                        # Zmieniam gracza wistującego następną lewę
                        new_first_lead_player = max(leads, key=lambda x: leads[x])

                        # Cofam priorytet koloru na kolejne lewy
                        self.back_priority(suit_of_lead)

                        # Usuwam każdą z kart w lewie
                        first_lead_player.remove_card(first_lead)
                        second_lead_player.remove_card(second_lead)
                        third_lead_player.remove_card(third_lead)
                        forth_lead_player.remove_card(forth_lead)

                        # Zwiększam odpowiednio zgarnięte lewy N-S lub E-W
                        # if str(self.leading_player) in ['n_player', 's_player']:
                        #     ns_tricks += 1
                        # else:
                        #     ew_tricks += 1

                        # Dodaję lewę do kontenera na jedną z 13 kolejnych lew
                        possible_plays.append([first_lead, second_lead, third_lead, forth_lead])

                        self.generate_plays(
                            possible_plays=possible_plays,
                            tricks_left=tricks_left-1,
                            ns_tricks=ns_tricks,
                            ew_tricks=ew_tricks,
                            first_lead_player=new_first_lead_player
                        )

                        # Przywracam usunięte karty
                        first_lead_player.add_card(first_lead)
                        second_lead_player.add_card(second_lead)
                        third_lead_player.add_card(third_lead)
                        forth_lead_player.add_card(forth_lead)

                        # Usuwam ostatnią - 13-tą lewę z pojemnika
                        possible_plays.pop()

    def start(self):
        # Zmieniam priorytet dla atutów, żeby zawsze miały największy
        self.change_priority_with_trump()

        # Rozpoczynam generowanie wszystkich możliwych rozgrywek
        self.generate_plays(
            possible_plays=[],
            ns_tricks=0,
            ew_tricks=0,
            tricks_left=3,
            first_lead_player=self.leading_player
        )

        print(len(self.possible_plays))

        # Wyświetlam ręce graczy
        print(f'N hand: {Player.instances[0].hand}')
        print(f'E hand: {Player.instances[1].hand}')
        print(f'S hand: {Player.instances[2].hand}')
        print(f'W hand: {Player.instances[3].hand}')
