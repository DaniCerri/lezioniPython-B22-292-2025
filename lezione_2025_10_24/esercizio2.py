# Lanciamo 8 dadi (D20 -> Il dado ha 20 facce) ed eliminiamo i lanci massimo e minimo

import random # libreria per utilizzare e ottenere valori casuali
lanci = []  # Inizializziamo una lista vuota
FACCE = 20  # Numero di facce del dado
N_LANCI = 8  # Numero di lanci del dado

for i in range(N_LANCI):
    # Lanciamo il dado
    risultato = random.randint(1, FACCE)  # Estraiamo un intero casuale da 1 al numero di FACCE

    # Aggiungiamo il risultato alla lista
    lanci.append(risultato)

print(f"Lanci eseguiti: {lanci}")

# Dobbiamo trovare il massimo e il minimo
# TODO: provare a trovare l'indice del minimo/massimo
minimo = lanci[0]
for lancio in lanci:
    if minimo > lancio:
        minimo = lancio

print(f"Lancio minimo: {minimo}")

massimo = lanci[0]
for lancio in lanci:
    if massimo < lancio:
        massimo = lancio

print(f"Lancio massimo: {massimo}")

# Rimuoviamo i valori dalla lista
lanci.remove(minimo)
lanci.remove(massimo)

print(f"Lanci rimasti: {lanci}")

# Calcoliamo la media dei lanci rimasti
media = sum(lanci) / len(lanci)
print(f"Lancio medio: {media:.2f}")

# TODO: Calcolare la deviazione standard (senza usare la funzione di math)


























# Formula deviazione standard: radice quadrata(somma((elemento - media) ** 2) / n_elementi)