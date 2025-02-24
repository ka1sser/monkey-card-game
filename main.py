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

    p1 = player.Player("Kai")
    p2 = player.Player("Wea")
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

    print(f"Distributing cards to: {players_list}")
    gm.distribute_cards(p1)
    gm.distribute_cards(p2)

    if len(gm.deck) != 0:
        random_player = random.choice([p1, p2])
        random_player.player_deck.append(gm.deck[0])
        gm.deck.pop(0)

    print(len(p1.player_deck))
    print(len(p2.player_deck))
