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

    print()
    print("Let us play!")
    print("Shuffling cards...")
    gm.shuffle_cards()
    game_deck = gm.deck
    print()

    print(f"Length of deck: {gm.length_of_deck()}")
    print()

    print("Hiding a card....")
    hidden_card = gm.hide_card()
    print(hidden_card)
    print(f"Length of deck: {gm.length_of_deck()}")
    print()

    for p in players_input:
        print(f"Distributing to {p.player_name}: ")
        gm.distribute_cards(p)
        print(f"Deck: {p.player_deck}")
        print(f"Length of deck: {len(p.player_deck)}")

    num_of_players = len(players_input)
    cards_per_player = 51 / num_of_players
    remainder = 51 % num_of_players

    print(f"Remaining num of cards: {remainder}")
    for x in range(remainder):
        random_player = random.choice(players_input)
        print(f"x: {x}, card: {gm.deck[x]}")
        random_player.player_deck.append(gm.deck[x])

    for p in players_input:
        print(f"\nDistributing to {p.player_name}: ")
        print(f"Length of deck: {len(p.player_deck)}\n")
        print(f"Deck:\n {p.player_deck}")

        print("\nCleaning pairs...")
        print("Remaining cards: ")
        rem_cards = p.check_initial_pairs()
        print(rem_cards)
        print(f"Length of deck: {len(rem_cards)}")

    print(hidden_card)
