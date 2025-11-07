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

# 4. Implementa una funzione `corso_piu_popolare()` che restituisce il nome del corso con il
# maggior numero totale di partecipanti (sommando tutte le fasce orarie e tutti i giorni)
def corso_piu_popolare(dizionario: dict) -> str:
    # 1. Calcoliamo l'affluenza totale per ogni corso
    diz_somme = {}  # Sarà il dizionario in cui salviamo le affluenze totali
    for corso, affluenze in dizionario.items():
        for affluenza_oraria in affluenze.values():  # Per ogni lista di affluenza (per fascia oraria)
            somma = sum(affluenza_oraria)  # Calcoliamo l'affluenza totale di questa fascia oraria

            # Cerchiamo di ottenere il totale parziale del corso di cui stiamo calcolando l'affluenza totale
            # Se non troviamo la chiave corrispondente al corso, vuol dire che è la prima volta che cerchiamo
            # di aggiungere al nostro totale parziale del corso, infatti di default [se non c'è la chiave]
            # restituiamo uno zero
            totale_parziale = diz_somme.get(corso, 0)

            totale_parziale += somma  # Aggiungiamo la somma della fascia oraria attuale al totale parziale
            diz_somme[corso] = totale_parziale  # Salviamo il totale parziale nel dizionario delle somme
            # Se la chiave con il corso attuale ancora non c'è, viene creata la coppia chiave - totale parziale

    # 2. Troviamo il corso con affluenza maggiore
    corso_migliore = list(diz_somme.keys())[0]  # Prendiamo un corso a caso e decidiamo che sia
    # il migliore PROVVISORIO

    for corso, affluenza_totale in diz_somme.items():  # Per ogni coppia corso-affluenza totale
        # Se l'affluenza del corso attuale è maggiore dell'affluenza del corso migliore fin'ora
        if affluenza_totale > diz_somme[corso_migliore]:
            corso_migliore = corso  # Abbiamo trovato il nuovo corso migliore fin'ora

    # Al termine del for, il corso che rimane come migliore sarà il migliore di tutti
    return corso_migliore

# 5. Implementa una funzione `giorno_migliore(corso, fascia_oraria)` che restituisce il giorno
# (posizione 0-4) con più partecipanti per quella combinazione corso-fascia
def giorno_migliore(corso: dict, fascia_oraria: str) -> int:
    dati = corso[fascia_oraria]  # Prendiamo i dati del corso alla fascia oraria richiesta -> lista di interi
    posizione_max = 0  # Decidiamo provvisoriamente di assegnare il massimo alla posizione 0 (primo elemento)
    for i in range(len(dati)):  # Per ogni indice fino alla lunghezza della lista (esclusa)
        # Se l'elemento della lista alla posizione attuale [i] è maggiore dell'elemento della lista
        # alla posizione del massimo (fin'ora) [posizione_max]
        if dati[i] > dati[posizione_max]:
            posizione_max = i  # Abbiamo trovato la nuova posizione del massimo

    return posizione_max

# 6. Implementa una funzione `analisi_completa()` che stampa un report con:
#    - Il corso più popolare in assoluto
#    - Per ogni corso, quale fascia oraria è più frequentata
#    - La media generale di partecipanti per ogni fascia oraria (considerando tutti i corsi)
def analisi_completa(dizionario: dict) -> str:
    """
    Funzione che prende un dizionario con le affluenze a dei corsi e restituisce un report completo in formato str.
    :param dizionario: Dizionario di affluenza
    :return: report, str
    """
    report = "-" * 50 + " Report sui corsi " + "-" * 50  # Inizializziamo la stringa del nostro report con il titolo
    report += "\n"

    # 1. Trovare il corso più frequentato
    miglior_corso = corso_piu_popolare(dizionario)
    # Aggiungiamo il risultato al nostro report
    report += f"Miglior corso: {miglior_corso}\n\n"

    # 2. Per ogni corso trovare la migliore fascia oraria
    report += f"Migliore fascia oraria per ogni corso\n"
    for nome_corso, dati_corso in dizionario.items():
        fascia_migliore = fascia_piu_frequentata(dati_corso)
        report += f" - {nome_corso}: {fascia_migliore}\n"

    report += "\n"

    # 3. Per ogni corso calcolare la media di affluenza per ogni fascia oraria
    report += f"Media delle fasce orarie: \n"
    for nome_corso, dati_corso in dizionario.items():
        report += f" * {nome_corso}: \n"
        for nome_fascia in dati_corso.keys():
            media_fascia = media_partecipanti(nome_corso, dati_corso, nome_fascia)
            report += f"  - Media {nome_fascia}: {media_fascia:.2f}\n"

    return report

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
    # media = media_partecipanti("Pilates", diz_affluenza['Pilates'], 'Pomeriggio')
    # print(media)
    #
    # migliore = fascia_piu_frequentata(diz_affluenza['Yoga'])
    # print(f"La fascia migliore per Yoga è {migliore}")
    #
    # miglior_corso = corso_piu_popolare(diz_affluenza)
    # print(f"Miglior corso: {miglior_corso}")
    #
    # giorno_migliore(diz_affluenza['Yoga'], 'Mattina')
    # print(diz_affluenza['Yoga'])

    report = analisi_completa(diz_affluenza)
    print(report)