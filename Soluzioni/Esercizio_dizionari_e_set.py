import random

ricette = {
    "Carbonara": {"pasta", "uova", "guanciale", "pecorino", "pepe"},
    "Pasta al pomodoro": {"pasta", "pomodoro", "basilico", "aglio", "olio"},
    "Tiramisu": {"uova", "mascarpone", "savoiardi", "caffe", "cacao"},
    "Frittata": {"uova", "olio", "sale", "parmigiano"},
    "Aglio e olio": {"pasta", "aglio", "olio", "peperoncino"}
}

dispensa = {"pasta", "uova", "olio", "sale", "aglio", "pepe", "parmigiano"}

## Esercizio 1
# Scrivi un programma che verifichi quali ricette puoi cucinare con gli
# ingredienti in dispensa e stampi cosa manca per quelle che non puoi preparare.
sep = "-" * 50
print(f"{sep} Esercizio 1 {sep}")
# Per ogni coppia ricetta <-> ingredienti necessari
for ricetta, ingredienti in ricette.items():
    # Se gli ingredienti sono un sottoinsieme di ciò che abbiamo in dispensa
    if ingredienti.issubset(dispensa):
        print(f"Possiamo fare la ricetta '{ricetta}'")  # Possiamo fare la ricetta
    else:  # Altrimenti, ci sono degli ingredienti che non sono nella dispensa
        # Li stampiamo
        # TODO bonus: stampare gli ingredienti mancanti con .join()
        print(f"Mancano degli ingredienti per '{ricetta}': {ingredienti - dispensa}")
print()

## Esercizio 2
# Trova gli ingredienti comuni tra due ricette a tua scelta.
# Noi utilizziamo random per scegliere casualmente le ricette

print(f"{sep} Esercizio 2 {sep}")
# Estraiamo due ricette DIVERSE
chiavi_ricette = random.sample(list(ricette.keys()), 2)

# Gli elementi comuni sono quelli dell'intersezione che in python si
# scrive con "&"
# Python andrà prima a prendere l'elemento a indice i per ottenere la chiave
# e successivamente va a prendere l'elemento del dizionario alla chiave
# ottenuta
elementi_comuni = ricette[chiavi_ricette[0]] & ricette[chiavi_ricette[1]]
# TODO bonus: capire (se esistono) quali sono gli ingredienti comuni a TUTTE le ricette

print(f"La ricetta '{chiavi_ricette[0]}' e la ricetta '{chiavi_ricette[1]}' hanno"
      f" in comune i seguenti ingredienti: {elementi_comuni}")
print()

## Esercizio 3
# Vuoi cucinare "Carbonara" e "Tiramisu". Calcola la lista della spesa completa
# (ingredienti che ti mancano per entrambe le ricette).
# TODO: fare in modo che le due ricette siano scelte casualmente
print(f"{sep} Esercizio 3 {sep}")

# Gli ingredienti necessari per fare ENTRAMBE le ricette sono quelli dell'unione delle due
ingredienti_necessari = ricette['Carbonara'] | ricette['Tiramisu']

# Capiamo quali sono gli ingredienti da comprare, eliminando dalla "lista" quelli che
# già sono nella dispensa
ingredienti_da_comprare = ingredienti_necessari - dispensa
print(f"Ingredienti da comprare: {ingredienti_da_comprare}")
print()

## Esercizio 7
# Trova tutte le coppie di ricette che NON hanno ingredienti in comune.
print(f"{sep} Esercizio 7 {sep}")
# TODO bonus: cambiando le liste di items, si può prendere ogni coppia una volta sola

for chiave_prima, elemento_primo in ricette.items():
    for chiave_seconda, elemento_secondo in ricette.items():
        if len(elemento_primo & elemento_secondo) == 0:
            print(f"'{chiave_prima}' non ha nessun ingrediente in comune con '{chiave_seconda}'")