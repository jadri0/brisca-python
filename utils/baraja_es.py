class card:
    alt_card_names = {
    1 : "As",
    10 : "Sota",
    11 : "Caballo",
    12 : "Rey"
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
    suits = ["oros", "copas", "espadas", "bastos"]
    return [card(number, suit) for suit in suits for number in range(1,13)]

deck = create_deck()