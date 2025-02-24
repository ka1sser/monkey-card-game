import random
import math
import cards
import player


class GameManager:

    def __init__(self):
        self.deck = cards.Cards().whole_deck

    def length_of_deck(self):
        return len(self.deck)

    def shuffle_cards(self):
        random.shuffle(self.deck)

    def hide_card(self):
        hidden_card = random.choice(self.deck)
        hidden_card_index = self.deck.index(hidden_card)
        self.deck.pop(hidden_card_index)

        return hidden_card

    def distribute_cards(self, p):

        num_of_players = len(player.Player.players_list)
        cards_per_player = math.floor(51 / num_of_players)

        for x in range(cards_per_player):
            p.player_deck.append(self.deck[x])

        self.deck = self.deck[cards_per_player:]
