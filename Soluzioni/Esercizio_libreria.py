# 2. Implementa una funzione `calcola_media_vendite(genere)`
# che restituisce la media delle vendite per quel genere
def calcola_media_vendite(genere: str, dizionario: dict) -> float:
    """
    Dato un genere e i dati di riferimento, calcola la media
    :param genere: Genere letterario
    :param dizionario: Dizionario con i dati per ogni genere
    :return: media, float
    """
    media = sum(dizionario[genere]) / len(dizionario[genere])
    return media

# 3. Implementa una funzione `genere_piu_venduto()` che restituisce il nome del
# genere con il maggior numero di vendite totali
def genere_piu_venduto(dizionario: dict) -> str:
    """
    Dati i dati di vendita, trova il genere con più vendite
    :param dizionario: dizionario con i dati di vendita
    :return: genere, str
    """
    # 1. Dobbiamo calcolare quante vendite ha fatto ogni genere
    vendite = {}  # Creiamo un dizionario vuoto in cui mettere i totali
    for genere, dati in dizionario.items():  # Per ogni genere e dati corrispondenti
        # Andiamo a creare nel dizionario vendite un nuovo campo con chiave il genere
        # corrente e valore la somma delle sue vendite
        vendite[genere] = sum(dati)

    # 2. Cerchiamo il genere con il valore più alto
    # Scegliamo un genere a caso e "fingiamo" che sia il massimo
    genere_massimo = list(vendite.keys())[0]
    for genere, tot_vendite in vendite.items():  # Per ogni genere e totale vendite
        # Se il dizionario alla chiave del massimo è minore del valore attuale
        if vendite[genere_massimo] < tot_vendite:
            # Vuol dire che abbiamo trovato il genere a cui si trova il massimo (fin'ora)
            genere_massimo = genere

    # 3. Restituiamo il genere trovato
    return genere_massimo

diz_vendite = {
    ### Dati delle vendite (ultimi 6 mesi)
    "Gialli": [45, 52, 38, 61, 49, 55],
    "Romanzi": [78, 82, 91, 88, 76, 85],
    "Fantascienza": [23, 28, 31, 26, 29, 34],
    "Saggistica": [15, 18, 22, 19, 17, 21],
}

