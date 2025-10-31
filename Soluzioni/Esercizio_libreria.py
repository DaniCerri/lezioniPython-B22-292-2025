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

# 4. Implementa una funzione `mese_migliore(genere)` che restituisce il mese
# (posizione nella lista) in cui quel genere ha venduto di più
def mese_migliore(genere: str, dizionario: dict) -> int:
    """
    Dati i dati di vendita e un genere, restituisce la posizione delle vendite migliori
    :param genere: Genere letterario
    :param dizionario: Dati delle vendite
    :return: indice del mese migliore, int
    """
    # 1. Otteniamo i dati del genere che ci interessa
    dati = dizionario[genere]  # Otteniamo la LISTA di vendite del genere

    # 2. Troviamo l'indice della lista con valore maggiore
    indice_max = 0  # Decidiamo di impostare come massimo provvisorio il primo elemento
    for i in range(len(dati)):  # Per ogni indice da 0 a lunghezza dei dati
        # Se il dato all'indice corrente è maggiore di quello all'indice del massimo
        if dati[i] > dati[indice_max]:
            # Abbiamo trovato l'indice del nuovo massimo e lo salviamo
            indice_max = i

    # 3. Restituiamo il valore ottenuto
    return indice_max


# 1. Facciamo una lista di mesi per la traduzione dell'indice del mese migliore
lista_mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile',
              'Maggio', 'Giugno', 'Luglio', 'Agosto',
              'Settembre', 'Ottobre', 'Novembre', 'Dicembre']

# 2. Facciamo un dizionario chiave-valore
diz_vendite = {
    "Gialli": [45, 9999, 38, 61, 49, 55, 12, 45, 76, 32, 323, 34, 2323, 23, 36, 8, 6, 575, 56, 90],
    "Romanzi": [78, 82, 91, 88, 76, 85, 12, 45, 76, 32, 323, 34, 12, 23, 36, 8, 6, 575, 56, 90],
    "Fantascienza": [23, 28, 31, 26, 29, 34, 12, 45, 76, 32, 323, 34, 4, 23, 36, 8, 6, 575, 56, 90],
    "Saggistica": [15, 18, 22, 19, 17, 21, 12, 45, 76, 32, 323, 34, 65, 23, 36, 8, 6, 575, 56, 90],
}

# Calcoliamo le vendite medie di ogni genere e il mese migliore
for genere in diz_vendite.keys():
    media = calcola_media_vendite(genere, diz_vendite)
    best_month = mese_migliore(genere, diz_vendite)

    print(f"Dati di {genere}:")
    print(f" - Media: {media:.2f}")
    print(f" - Mese migliore: {lista_mesi[best_month % 12]} del {best_month // 12 + 1} anno di apertura")

print()

# Trovare il mese migliore
best_genre = genere_piu_venduto(diz_vendite)
print(f"Il genere con più vendite è {best_genre} con {sum(diz_vendite[best_genre])} vendite")

