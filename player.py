import math
import game_manager
from collections import defaultdict


class Player:

    players_list = []

    def __init__(self, player_name):
        self.player_name = player_name
        self.player_deck = []

        self.players_list.append(self.player_name)

    def get_player(self):
        return self

    def get_player_deck(self, player_name):
        if self.player_name == player_name:
            return self.player_deck

    def check_initial_pairs(self):

        # Dictionary to track the number of occurrences
        values_counts = defaultdict(int)

        for card in self.player_deck:
            for key, value in card.items():
                # Adds one for each occurence of the value
                values_counts[value] += 1

        # Dictionary to track what values to remove
        values_to_remove = defaultdict(int)

        for value, count in values_counts.items():
            # Checks if even, meaning all cards will be removed since they can all be paired
            if count % 2 == 0:
                values_to_remove[value] = count
            else:
                # Gets the whole number to be multiplied by 2 to get the number of pairs
                # Ex: count = 3, floor = (3/2) = 1, since there's 1 pair, it is multiplied
                # by 2 to show that it's a pair
                floor = math.floor(count / 2)
                values_to_remove[value] = floor * 2

        filtered_deck = []

        for card in self.player_deck:
            for key, value in card.items():
                if values_to_remove[value] > 0:
                    values_to_remove[value] -= 1
                else:
                    filtered_deck.append(card)

        return filtered_deck

    @classmethod
    def get_player_list(cls):
        return cls.players_list
