import random

ALL_CARDS = [ number + suit for number in list("A23456789JQK") + ["10"] for suit in "SCHD"]

class Game:
    def __init__(self, game_id, players):
        self.game_id = game_id
        self.players = players
        self.cards = {
                "pickup_pile": ALL_CARDS.copy(),
                "played_cards": []
        }
        random.shuffle(self.cards["pickup_pile"])
        for player in players:
            self.cards[player] = []

    def play(self, player, card):
        self.cards[player].remove(card)
        self.cards["played_cards"].append(card)

    def undo(self, player):
        card = self.cards["played_cards"].pop(-1)
        self.cards[player].append(card)

    def pickup(self, player):
        card = self.cards["pickup_pile"].pop(-1)
        self.cards[player].append(card)

    def shuffle_deck(self):
        cards = self.cards["played_cards"].copy()
        self.cards["played_cards"] = []
        random.shuffle(cards)
        self.cards["pickup_pile"] = cards

    @property
    def last_card(self):
        if self.cards["played_cards"] == []:
            return "XX"
        return self.cards["played_cards"][-1]

    def cards_for(self, player):
        return self.cards[player]

    def __str__(self):
        return f"Game {self.game_id} " + str(self.cards)

    def __repr__(self):
        return f"Game {self.game_id} " + str(self.cards)