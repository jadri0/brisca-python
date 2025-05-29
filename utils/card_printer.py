from utils import baraja_es
from utils import baraja_fr

symbols = {
    "bastos" : "¶",
    "oros" : "O",
    "espadas" : "†",
    "copas" : "Y",
    "picas" : "♠",
    "diamantes" : "♦",
    "tréboles" : "♣",
    "corazones" : "♥"
}

values_fr = {
    1 : "A",
    11 : "J",
    12 : "Q",
    13 : "K"
}

def print_card(card):

    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"

    if card in baraja_fr.deck:
        if card.number == 10:
            number_right = str(card.number)
            number_left = str(card.number)
        else:
            number_right = str(values_fr.get(card.number, str(card.number))) + " "
            number_left = " " + str(values_fr.get(card.number, str(card.number)))

        suit_line = f"│    {symbols.get(card.suit)}    │"
        number_line_left = f"│{number_left}       │"
        number_line_right = f"│       {number_right}│"

        print(top)
        print(number_line_left)
        print(side)
        print(suit_line)
        print(side)
        print(number_line_right)
        print(bottom)
    
    else:
        if card.number in [10, 11, 12]:
            number_right = str(card.number)
            number_left = str(card.number)
        else:
            number_right = str(card.number) + " "
            number_left = " " + str(card.number)

        suit_line = f"│    {symbols.get(card.suit)}    │"
        number_line_left = f"│{number_left}       │"
        number_line_right = f"│       {number_right}│"

        print(top)
        print(number_line_left)
        print(side)
        print(suit_line)
        print(side)
        print(number_line_right)
        print(bottom)

def print_cards_inline(cards):
    lines = [[] for _ in range(7)]

    for card in cards:
        if card in baraja_fr.deck:
            number = values_fr.get(card.number, str(card.number))
        else:
            number = card.number

        number_left = f"{number:<2}"[:2]
        number_right = f"{number:>2}"[:2]
        symbol = symbols.get(card.suit, "?")

        lines[0].append("┌─────────┐")
        lines[1].append(f"│{number_left}       │")
        lines[2].append("│         │")
        lines[3].append(f"│    {symbol}    │")
        lines[4].append("│         │")
        lines[5].append(f"│       {number_right}│")
        lines[6].append("└─────────┘")

    for line in lines:
        print(" ".join(line))