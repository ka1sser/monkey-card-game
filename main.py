import time
import random
import cards
import game_manager
import player


gm = game_manager.GameManager()

if __name__ == "__main__":
    cards = cards.Cards()

    print("**********************************")
    print("******** MONKEY CARD GAME ********")
    print("**********************************\n")

    num_player = int(input("How many players?: "))
    players_input = []
    if num_player <= 1:
        print("Players must be 2 or higher.")
    else:
        for x in range(num_player):
            player_name = input("Enter player name: ")
            players_input.append(player.Player(player_name))

    players_list = player.Player.players_list

    print()
    print("Let us play!")
    print("Shuffling cards...")
    gm.shuffle_cards()
    game_deck = gm.deck
    print()

    print(f"Length of deck: {gm.length_of_deck()}")
    print()
    time.sleep(1)

    print("Hiding a card....")
    print(gm.hide_card())
    print(f"Length of deck: {gm.length_of_deck()}")
    time.sleep(1)
    print()

    for p in players_input:
        print(f"Distributing to {p.player_name}: ")
        gm.distribute_cards(p)
        print(f"Deck: {p.player_deck}")
        print(f"Length of deck: {len(p.player_deck)}")
