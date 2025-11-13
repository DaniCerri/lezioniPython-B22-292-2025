# Funzione 1: conta_vocali (10 punti)
# Prende come parametro una stringa
# Restituisce il numero di vocali (a, e, i, o, u) presenti nella stringa
# Deve essere case-insensitive (maiuscole e minuscole contano allo stesso modo)
from operator import itemgetter


def conta_vocali(stringa: str) -> int:
    """
    Conta il numero di vocali di vocali in una stringa
    :param stringa: stringa qualunque
    :return: numero di vocali, int
    """
    VOCALI = ('a', 'e', 'i', 'o', 'u')  # Le vocali da contare
    counter = 0  # Inizializziamo a 0 il contatore che terrà conto di TUTTE le vocali

    # for vocale in VOCALI:
    #     for lettera in stringa:
    #         if lettera.lower() == vocale:
    #             counter += 1
    #
    # for lettera in stringa:
    #     if lettera.lower() in VOCALI:
    #         counter += 1

    for vocale in VOCALI:
        counter += stringa.lower().count(vocale)

    return counter

# Funzione 2: filtra_maggiorenni (14 punti)
#
# Prende come parametro una lista di dizionari con le chiavi "nome" e "eta"
# Restituisce una nuova lista contenente solo le persone con età maggiore
# o uguale a 18 anni
# La lista deve essere ordinata per età crescente
def filtra_maggiorenni(dizionari: list[dict]) -> list:
    # 1. troviamo quelli che hanno un'età >= 18 anni
    maggiorenni = []
    for persona in dizionari:
        if persona['eta'] >= 18:
            maggiorenni.append(persona)

    # 2. Ordiniamo i maggiorenni
    # -> utilizziamo il metodo sorted
    maggiorenni = sorted(maggiorenni, key=itemgetter('eta'))  # Ordiniamo in base al parametro eta

    # 3. restituiamo la lista ordinata
    return maggiorenni

# Funzione 3: somma_dispari (10 punti)
#
# Prende due parametri: inizio e fine (numeri interi)
# Restituisce la somma di tutti i numeri dispari compresi tra inizio e fine (estremi inclusi)
# Se non ci sono numeri dispari nell'intervallo, restituisce 0
def somma_dispari(inizio: int, fine: int) -> int:
    """
    Dati un inizio e una fine, calcola la somma di tutti i numeri dispari nel range [inizio, fine] (inizio, fine)
    :param inizio: primo numero (COMPRESO)
    :param fine: ultimo numero (COMPRESO)
    :return: somma dei numeri dispari, int
    """
    tot = 0

    # for i in range(inizio, fine + 1):
    #     if i % 2 == 1:
    #        tot += i

    if inizio % 2 == 0:
        inizio += 1

    for i in range(inizio, fine + 1, 2):
        tot += i

    return tot


if __name__ == "__main__":
    parola = 'Aiuola'
    print(f"Vocali in '{parola}': {conta_vocali(parola)}")

    persone = [
        {"nome": "Daniele", "eta": 21},
        {"nome": "Ilaria", "eta": 3},
        {"nome": "Marco", "eta": 19},
        {"nome": "Giulia", "eta": 36},
    ]

    print(f"I maggiorenni della lista sono: {filtra_maggiorenni(persone)}")

    inizio = 2
    fine = 9
    print(f"La somma dei dispari nel range [{inizio}, {fine}] è: {somma_dispari(inizio, fine)}")