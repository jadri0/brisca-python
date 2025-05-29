import os
import sys

# Limpia la consola. Funciona tanto en Windows como en Linux.
def clear():
    os.system("clear||cls")

# Esta función permite hacer un loop y evitar el mensaje de error al pulsar Ctrl + C dentro del input("\nPresiona [Intro] para salir...") de keyboard_exception().
def exit():
    while True:
        try:
            sys.exit(0)
        except KeyboardInterrupt:
            exit()

# Importante poner esto debajo del except KeyboardInterrupt del programa principal (el resto de la función main() iría debajo de try), y asegurarse de haber importado sys y exit().
def keyboard_exception():
    while True:
            try:
                input("\nPresiona [Intro] para salir...")
                sys.exit(0)
            except KeyboardInterrupt:
                exit()