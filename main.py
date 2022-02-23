import random
import os

deck = [
    'K♢', 'Q♢', 'J♢', '10♢', '9♢', '8♢', '7♢', '6♢', '5♢', '4♢', '3♢', '2♢',
    'A♢', 'K♧', 'Q♧', 'J♧', '10♧', '9♧', '8♧', '7♧', '6♧', '5♧', '4♧', '3♧',
    '2♧', 'A♧', 'K♡', 'Q♡', 'J♡', '10♡', '9♡', '8♡', '7♡', '6♡', '5♡', '4♡',
    '3♡', '2♡', 'A♡', 'K♤', 'Q♤', 'J♤', '10♤', '9♤', '8♤', '7♤', '6♤', '5♤',
    '4♤', '3♤', '2♤', 'A♤'
]
player_one_hand = []
player_two_hand = []
table_cards = []
cards_left = 52


def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


def shuffle_deck(deck):
    shuffled_deck = []
    i = 0
    x = 0

    times = random.randint(1, 13)

    if times == 0:
        print(deck)

    while x < times:
        for card in deck:
            i += 1

            if i % 2 == 0:
                shuffled_deck = [card] + shuffled_deck

            elif i % 2 == 1:
                shuffled_deck.append(card)

            else:
                print("Error")
                break

        x += 1

        deck = shuffled_deck

        if x == times:
            shuffled_deck = []
            return deck

        else:
            shuffled_deck = []


def start_game(deck, cards_left, player_one_hand, player_two_hand):
    x = 0

    while x < 4:
        card = random.randint(0, cards_left - 1)

        if x % 2 == 0:
            player_one_hand.append(deck[card])

        elif x % 2 == 1:
            player_two_hand.append(deck[card])

        else:
            print("ERROR")

        deck.pop(card)
        cards_left -= 1
        x += 1

    input(
        "Player two turn around. When only player one can see press enter.\n")
    print("Player one: " + str(player_one_hand) + "\n")
    input(
        "Press enter when ready. Player one turn around and get player two to turn back around."
    )
    clear()
    input("When only player two can see press enter.\n")
    print("Player two: " + str(player_two_hand) + "\n")
    input(
        "Press enter when ready. Player two get player two to turn back around after pressing enter."
    )
    clear()

    return cards_left, player_one_hand, player_two_hand, deck


def flop(deck, table_cards, cards_left):
    x = 0
    while x < 3:
        card = random.randint(0, cards_left - 1)
        table_cards.append(deck[card])

        deck.pop(card)
        x += 1
        cards_left -= 1

    return table_cards


def turn(deck, table_cards, cards_left):
    card = random.randint(0, cards_left - 1)
    table_cards.append(deck[card])

    deck.pop(card)
    cards_left -= 1

    return table_cards


def river(deck, table_cards, cards_left):
    card = random.randint(0, cards_left - 1)
    table_cards.append(deck[card])

    deck.pop(card)
    cards_left -= 1

    return table_cards

if __name__ == "__main__":
    clear()
    shuffle_deck(deck)

    start_game(deck, cards_left, player_one_hand, player_two_hand)

    flop(deck, table_cards, cards_left)
    input("Table cards:\n" + str(table_cards))
    clear()

    turn(deck, table_cards, cards_left)
    input("Table cards:\n" + str(table_cards))
    clear()

    river(deck, table_cards, cards_left)
    input("Table cards:\n" + str(table_cards) + "\n\nPlayer one hand: " +
        str(player_one_hand) + "\n\nPlayer two hand: " + str(player_two_hand))
    clear()
