import math
import game_manager

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
    
    @classmethod
    def get_player_list(cls):
        return cls.players_list