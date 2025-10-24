# Creiamo un personaggio casuale per una campagna di un famoso gioco di ruolo
import random

# 1. Estraiamo un nome da una lista [possiamo estrarre l'indice della lista]
# 2. Diamo un punteggio casuale di Forza, Intelligenza, Destrezza, Costituzione da 1 a 20
# 3. Facciamo 4 lanci di dadi da 14 facce, se la somma è minore di 35 il personaggio muore,
# a meno che non abbia almeno una caratteristica a più di 15, in tal caso sopravvive.

nomi = ['Giulia', 'Ilaria', 'Luca', 'Marco', 'Chiara', 'Giacomo']
lunghezza = len(nomi)
estratto = random.randint(0, lunghezza - 1)  # Mettiamo il -1 perchè l'estremo è compreso nell'estrazione
nome = nomi[estratto]

statistiche = []
for i in range(4):
    statistiche.append(random.randint(1, 20))

lanci = []
for i in range(4):
    lanci.append(random.randint(1, 14))

totale = sum(lanci)

# il minimo di una lista si trova con min(lista)
car_minima = min(statistiche)
if car_minima > 15 or totale >= 35:
    print(f"{nome} è sopravvissuta/o")  # TODO: fare un check per a/o
else:
    print(f"{nome} non ce l'ha fatta")

