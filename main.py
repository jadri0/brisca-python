from utils import baraja_es as baraja
from utils import card_printer as pr
from utils import exit_reset as exre
import random

def fin():
    fin = input("\n[s]alir      [r]eset\n\n").strip().lower()
    if fin in ["r", "reset"]:
        main()
    if fin in ["s", "salir"]:
        exre.exit()
    else:
        raise KeyboardInterrupt

def mostrar_cartas():
    print("Tu mano:\n")
    pr.print_cards_inline(cartas_jugador)

def mostrar_carta_cpu():
    print("La CPU juega:\n")
    pr.print_card(carta_jugada_cpu)
    print(carta_jugada_cpu)

def repartir_cartas():
    global carta_triunfo, palo_triunfo, cartas_cpu, cartas_jugador, carta_jugada_cpu, deck
    deck = baraja.create_deck()
    random.shuffle(deck)
    cartas_jugador = [deck[0], deck[2], deck[4]]
    cartas_cpu = [deck[1], deck[3], deck[5]]
    carta_triunfo = deck[6]
    palo_triunfo = carta_triunfo.suit
    elegir_carta1_cpu()
    pr.print_card(carta_triunfo)
    print(carta_triunfo)
    print(f"\nTriunfo: [{pr.symbols.get(carta_triunfo.suit)}] {palo_triunfo.capitalize()}")
    print(separador)
    mostrar_carta_cpu()
    deck.remove(carta_triunfo)
    for carta in cartas_jugador:
        deck.remove(carta)
    for carta in cartas_cpu:
        deck.remove(carta)
    print(separador)

def jugar_carta():
    global carta_jugada, carta1, carta2, index_carta_jugada, index_carta_cpu
    while True:
        mostrar_cartas()
        print(separador)
        print(f"Carta triunfo: [{carta_triunfo.number}-{pr.symbols.get(carta_triunfo.suit)}] {carta_triunfo} ({palo_triunfo.capitalize()})")
        if carta_jugada_cpu != "":
            print(f"Carta CPU: [{carta_jugada_cpu.number}-{pr.symbols.get(carta_jugada_cpu.suit)}] {carta_jugada_cpu} ({carta_jugada_cpu.suit.capitalize()})\n")
        else:
            print("\nEmpiezas tú.\n")
        if len(cartas_jugador) == 3:
            carta_jugada = input(f"¿Qué carta vas a jugar?:\n\n[1] {cartas_jugador[0]}    [2] {cartas_jugador[1]}    [3] {cartas_jugador[2]}\n\n").strip()
            if carta_jugada not in ["1", "2", "3"]:
                print("\nCreo que no te he entendido bien...")
                print(separador)
            else:
                carta_jugada = cartas_jugador[int(carta_jugada) - 1]
                if carta_jugada_cpu == "":
                    elegir_carta2_cpu()
                    carta1 = carta_jugada
                    carta2 = carta_jugada_cpu
                else:
                    carta1 = carta_jugada_cpu
                    carta2 = carta_jugada
                print(separador)
                pr.print_cards_inline([carta1, carta2])
                print(f"{carta1}" + f"  {carta2}")
                index_carta_jugada = cartas_jugador.index(carta_jugada)
                index_carta_cpu = cartas_cpu.index(carta_jugada_cpu)
                cartas_cpu.remove(carta_jugada_cpu)
                cartas_jugador.remove(carta_jugada)
                break
        elif len(cartas_jugador) == 2:
            carta_jugada = input(f"¿Qué carta vas a jugar?:\n\n[1] {cartas_jugador[0]}    [2] {cartas_jugador[1]}\n\n").strip()
            if carta_jugada not in ["1", "2"]:
                print("\nCreo que no te he entendido bien...")
                print(separador)
            else:
                carta_jugada = cartas_jugador[int(carta_jugada) - 1]
                if carta_jugada_cpu == "":
                    elegir_carta2_cpu()
                    carta1 = carta_jugada
                    carta2 = carta_jugada_cpu
                else:
                    carta1 = carta_jugada_cpu
                    carta2 = carta_jugada
                print(separador)
                pr.print_cards_inline([carta1, carta2])
                print(f"{carta1}" + f"  {carta2}")
                index_carta_jugada = cartas_jugador.index(carta_jugada)
                index_carta_cpu = cartas_cpu.index(carta_jugada_cpu)
                cartas_cpu.remove(carta_jugada_cpu)
                cartas_jugador.remove(carta_jugada)
                break
        else:
            carta_jugada = input(f"Solo te queda una carta por jugar:\n\n[1] {cartas_jugador[0]}\n\n").strip()
            if carta_jugada not in ["1"]:
                print("\nNo lo hagas más difícil...")
                print(separador)
            else:
                carta_jugada = cartas_jugador[int(carta_jugada) - 1]
                if carta_jugada_cpu == "":
                    elegir_carta2_cpu()
                    carta1 = carta_jugada
                    carta2 = carta_jugada_cpu
                else:
                    carta1 = carta_jugada_cpu
                    carta2 = carta_jugada
                print(separador)
                pr.print_cards_inline([carta1, carta2])
                print(f"{carta1}" + f"  {carta2}")
                index_carta_jugada = cartas_jugador.index(carta_jugada)
                index_carta_cpu = cartas_cpu.index(carta_jugada_cpu)
                break

def gana_jugador():
    global carta_jugada, carta_jugada_cpu, puntos_cpu, puntos_jugador
    puntos_jugador += int(puntos.get(carta1.number, 0)) + int(puntos.get(carta2.number, 0))
    print(f"\n¡Has ganado la ronda!\n\n(+{int(puntos.get(carta1.number, 0)) + int(puntos.get(carta2.number, 0))})\n")
    print(f"[JUGADOR]    {puntos_jugador} - {puntos_cpu}    [CPU]")
    print(separador)
    carta_jugada_cpu = ""
    carta_jugada = ""

def gana_cpu():
    global carta_jugada, carta_jugada_cpu, puntos_cpu, puntos_jugador
    puntos_cpu += int(puntos.get(carta1.number, 0)) + int(puntos.get(carta2.number, 0))
    print("\nHas perdido la ronda...\n")
    print(f"[JUGADOR]    {puntos_jugador} - {puntos_cpu}    [CPU]")
    print(separador)
    elegir_carta1_cpu()
    carta_jugada = ""

def calcular_ronda():
    if carta1.suit == carta2.suit:
        if carta_jugada.number not in [1, 3] and carta_jugada_cpu.number not in [1, 3]:
            if carta_jugada.number > carta_jugada_cpu.number:
                gana_jugador()
            else:
                gana_cpu()
        elif carta_jugada.number in [1, 3] and carta_jugada_cpu.number not in [1, 3]:
            gana_jugador()
        elif carta_jugada.number not in [1, 3] and carta_jugada_cpu.number in [1, 3]:
            gana_cpu()
        else:
            if carta_jugada.number == 1:
                gana_jugador()
            else:
                gana_cpu()
    elif carta2.suit == palo_triunfo:
        if carta2 == carta_jugada:
            gana_jugador()
        else:
            gana_cpu()
    else:
        if carta1 == carta_jugada:
            gana_jugador()
        else:
            gana_cpu()

def robar_carta():
    global robada_jugador, robada_cpu
    if carta_jugada_cpu == "":
        cartas_jugador.insert(index_carta_jugada, random.choice(deck))
        robada_jugador = cartas_jugador[index_carta_jugada]
        deck.remove(robada_jugador)
        cartas_cpu.insert(index_carta_cpu, random.choice(deck))
        robada_cpu = cartas_cpu[index_carta_cpu]
        deck.remove(robada_cpu)
    else:
        cartas_cpu.insert(index_carta_cpu, random.choice(deck))
        robada_cpu = cartas_cpu[index_carta_cpu]
        deck.remove(robada_cpu)
        cartas_jugador.insert(index_carta_jugada, random.choice(deck))
        robada_jugador = cartas_jugador[index_carta_jugada]
        deck.remove(robada_jugador)
    print(f"Cartas restantes: {len(deck)}")
    print(separador)

def elegir_carta1_cpu():
    global carta_jugada_cpu
    posibles_jugadas_cpu = []
    for card in cartas_cpu:
        if card.number not in [1, 3, 10, 11, 12] and card.suit != palo_triunfo:
            posibles_jugadas_cpu.append(card)
        elif card.number not in [1, 3] and card.suit != palo_triunfo:
            posibles_jugadas_cpu.append(card)
        elif card.suit == palo_triunfo and card.number not in [1, 3, 10, 11, 12]:
                posibles_jugadas_cpu.append(card)
    if not posibles_jugadas_cpu:
        if min(cartas_cpu, key=lambda card: card.number) not in [1, 3]:
            carta_jugada_cpu = min(cartas_cpu, key=lambda card: card.number)
        else:
            carta_jugada_cpu = random.choice(cartas_cpu)
    else:
        posibles_jugadas_cpu.sort(key=lambda card: card.number)
        carta_jugada_cpu = posibles_jugadas_cpu[0]

def elegir_carta2_cpu():
    global carta_jugada_cpu
    posibles_jugadas_cpu = []
    if carta1.number in [1, 3, 10, 11, 12]:
        for card in cartas_cpu:
            if card.suit == palo_triunfo and carta1.suit != palo_triunfo and card.number not in [1, 3, 10, 11, 12]:
                posibles_jugadas_cpu.append(card)
            elif card.suit == carta1.suit and card.suit != palo_triunfo and carta1.number not in [1, 3] and card.number > carta1.number:
                posibles_jugadas_cpu.append(card)
            elif card.suit == palo_triunfo and carta1.suit != palo_triunfo and card.number not in [1, 3]:
                posibles_jugadas_cpu.append(card)
    else:
        for card in cartas_cpu:
            if card.number not in [1, 3, 10, 11, 12]:
                posibles_jugadas_cpu.append(card)
    if not posibles_jugadas_cpu:
        if min(cartas_cpu, key=lambda card: card.number) not in [1, 3]:
            carta_jugada_cpu = min(cartas_cpu, key=lambda card: card.number)
        else:
            carta_jugada_cpu = random.choice(cartas_cpu)
    else:
        posibles_jugadas_cpu.sort(key=lambda card: card.number)
        carta_jugada_cpu = posibles_jugadas_cpu[0]

def main():
    global puntos, carta_jugada, carta_jugada_cpu, carta1, carta2, carta_triunfo, puntos_cpu, puntos_jugador, separador
    try:
        puntos = {
            1 : 11,
            3 : 10,
            10 : 2,
            11 : 3,
            12 : 4
        }

        carta_jugada = ""
        carta_jugada_cpu = ""

        carta1 = ""
        carta2 = ""

        carta_triunfo = ""

        puntos_cpu = 0
        puntos_jugador = 0

        separador = "\n**************************************************************\n"

        exre.clear()
        print("""
  _             ____       _               
 | |    __ _   | __ ) _ __(_)___  ___ __ _ 
 | |   / _` |  |  _ \| '__| / __|/ __/ _` |
 | |__| (_| |  | |_) | |  | \__ \ (_| (_| |
 |_____\__,_|  |____/|_|  |_|___/\___\__,_|
                                                  
""")
        repartir_cartas()
        jugar_carta()
        calcular_ronda()
        robar_carta()

        while True:
            if len(deck) == 1 and len(cartas_cpu) > 0 and len(cartas_jugador) > 0:
                if carta_jugada_cpu != "":
                    mostrar_carta_cpu()
                    print(separador)
                jugar_carta()
                calcular_ronda()
                print(f"Ya no quedan cartas en el mazo.")
                print(separador)
                if carta_jugada_cpu != "":
                    mostrar_carta_cpu()
                    print(separador)
                jugar_carta()
                calcular_ronda()
                if carta_jugada_cpu != "":
                    mostrar_carta_cpu()
                    print(separador)
                jugar_carta()
                calcular_ronda()
                break
            if carta_jugada_cpu != "":
                mostrar_carta_cpu()
                print(separador)
            jugar_carta()
            calcular_ronda()
            robar_carta()
        print("¡Se han acabado las cartas!")
        print(separador)
        print(f"Recuento de puntos:\n\n[JUGADOR]    {puntos_jugador} - {puntos_cpu}    [CPU]")
        print(separador)
        if puntos_jugador > puntos_cpu:
            print("¡Felicidades, has ganado la partida!")
        elif puntos_jugador < puntos_cpu:
            print("Vaya... Has perdido la partida...")
        else:
            print("Pues parece que hemos empatado... ¿Quieres echar otra partida?")
        fin()

    except KeyboardInterrupt:
        exre.keyboard_exception()

main()