# Jogo de adivinhação

import random

numero_ad = random.randint(1, 100)
numero_r = int(input(f'Qual o número?: '))

while numero_r != numero_ad:  
    if numero_ad < numero_r:
       numero_r = int(input("Tente um número menor: "))
    elif numero_ad > numero_r:
       numero_r = int(input("Tente um número maior: "))

print('Parabéns, você acertou!!!')

