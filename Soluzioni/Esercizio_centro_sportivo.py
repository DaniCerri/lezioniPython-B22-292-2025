# 2. Implementa una funzione `media_partecipanti(corso, fascia_oraria)`
# che calcola la media dei partecipanti per un corso specifico
# in una fascia oraria specifica

def media_partecipanti(nome_corso: str, corso: dict, fascia_oraria: str) -> float:
    """
    Calcola la media di una fascia oraria di un corso dato
    :param nome_corso: Nome del corso di riferimento
    :param corso: Dizionario con i dati del corso
    :param fascia_oraria: Fascia oraria di riferimento
    :return: Media dell'affluenza, float
    """
    # Otteniamo i dati di cui calcolare la media dal dizionario con tutti i dati del corso,
    # andando a prendere la lista della fascia oraria che ci serve
    lista_dati = corso[fascia_oraria]
    media = sum(lista_dati) / len(lista_dati)  # Calcoliamo la media come sempre
    return media  # Restituiamo la media

# TODO: provare a implementare la funzione con questi parametri
# def media_partecipanti(corso: str, fascia_oraria: list[int]):

# 3. Implementa una funzione `fascia_piu_frequentata(corso)` che restituisce
# il nome della fascia oraria più frequentata per quel corso (basandosi sulla media)
def fascia_piu_frequentata(corso: dict) -> str:
    """
    Dato un corso, trova la fascia oraria che ha media di frequentazione più alta
    :param corso: Dizionario con i dati del corso
    :return: fascia più frequentata, str
    """
    # 1. Calcoliamo la media per ogni fascia oraria
    # 2. Cerchiamo la fascia oraria che ha come valore il massimo (delle medie)
    fascia_migliore = list(corso.keys())[0]  # Ne scegliamo una a caso
    for fascia_attuale in corso.keys():  # Per ogni fascia oraria disponibile
        # Calcoliamo la media della fascia migliore
        media_migliore = media_partecipanti("", corso, fascia_migliore)
        # Calcoliamo la media della fascia attuale
        media_attuale = media_partecipanti("", corso, fascia_attuale)

        if media_migliore < media_attuale: # se la fascia attuale ha media migliore (più alta)
            # La nuova fascia migliore è quella attuale
            fascia_migliore = fascia_attuale

    # 3. Restituiamo la fascia oraria trovata
    return fascia_migliore

diz_affluenza = {
    "Yoga": {
        "Mattina": [12, 15, 13, 14, 16],
         "Pomeriggio": [8, 9, 7, 10, 9],
         "Sera": [18, 20, 19, 21, 22],
    },
    "Pilates":{
        "Mattina": [10, 11, 9, 12, 10],
         "Pomeriggio": [15, 14, 16, 15, 17],
         "Sera": [20, 22, 21, 23, 24],
    },
    "Spinning":{
        "Mattina": [8, 9, 7, 8, 10],
         "Pomeriggio": [12, 14, 13, 15, 14],
         "Sera": [25, 28, 26, 27, 29],
    },
    "CrossFit":{
        "Mattina": [14, 16, 15, 17, 16],
         "Pomeriggio": [18, 19, 17, 20, 19],
         "Sera": [22, 24, 23, 25, 26],
    },
    "Zumba":{
        "Mattina": [6, 7, 5, 8, 7],
         "Pomeriggio": [20, 22, 21, 23, 22],
         "Sera": [16, 18, 17, 19, 18],
    }
}

if __name__ == "__main__":
    media = media_partecipanti("Pilates", diz_affluenza['Pilates'], 'Pomeriggio')
    print(media)

    migliore = fascia_piu_frequentata(diz_affluenza['Yoga'])
    print(f"La fascia migliore per Yoga è {migliore}")