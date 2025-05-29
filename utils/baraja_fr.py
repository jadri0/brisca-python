class card:
    alt_card_names = {
    1 : "As",
    11 : "Sota",
    12 : "Reina",
    13 : "Rey"
    }
   
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
 
    @property
    def value(self):
        return self.alt_card_names.get(self.number, str(self.number))

    def __str__(self):
        return f"{self.value} de {self.suit}"

    def __repr__(self):
        return str(self)

def create_deck():
    suits = ["corazones", "tréboles", "picas", "diamantes"]
    return [card(number, suit) for suit in suits for number in range(1,14)]

deck = create_deck()