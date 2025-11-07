# Dato un dizionario di consumi mensili
consumi = {
    "Gennaio": [12, 2, 3, 42, 21, 42],
    "Febbraio": [45, 12, 4],
    "Marzo": [69, 2, 12, 36, 45, 46],
    "Aprile": [457, 54, 12, 54, 6],
    "Maggio": [9, 4, 4, 45, 6, 2],
    "Giugno": [78, 65, 21, 32, 54, 69],
    "Luglio": [45, 12, 2],
    "Agosto": [4],
    "Settembre": [45, 3, 6, 9],
    "Ottobre": [4, 45, 6, 4],
    "Novembre": [9, 2],
    "Dicembre": [45, 6, 3, 65, 65],
}

def calcola_consumo_aggregato(diz_consumi: dict) -> dict:
    diz_aggregato = {}  # Dizionario vuoto in cui salveremo i consumi aggregati
    # per ogni coppia mese - consumi del mese
    for mese, lista_consumi in diz_consumi.items():
        # Creiamo un nuovo campo con il nome del mese e ci assegniamo il valore della somma
        # dei suoi consumi
        diz_aggregato[mese] = sum(lista_consumi)

    return diz_aggregato  # Restituiamo il dizionario ottenuto

# 1. Troviamo il mese con più consumo e il suo valore
def mese_piu_consumo(diz_consumi: dict) -> str:
    diz_aggregato = calcola_consumo_aggregato(diz_consumi)  # Calcoliamo i consumi totali per ogni mese

    mese_max = list(diz_aggregato.keys())[0]  # Prendiamo una chiave a caso e la assegniamo al massimo provvisorio

    for mese, consumo_tot in diz_aggregato.items():
        if consumo_tot > diz_aggregato[mese_max]:
            mese_max = mese

    return mese_max

# 2. Troviamo il mese con meno consumo e il suo valore
def mese_meno_consumo(diz_consumi: dict) -> str:
    diz_aggregato = calcola_consumo_aggregato(diz_consumi)  # Calcoliamo i consumi totali per ogni mese

    mese_min = list(diz_aggregato.keys())[0]  # Prendiamo una chiave a caso e la assegniamo al massimo provvisorio

    for mese, consumo_tot in diz_aggregato.items():
        if consumo_tot < diz_aggregato[mese_min]:
            mese_min = mese

    return mese_min

# 3.1. Calcoliamo il consumo medio dell'aggregato
def media_aggregato(diz_consumi: dict) -> float:
    diz_aggregato = calcola_consumo_aggregato(diz_consumi)
    media = sum(diz_aggregato.values()) / len(diz_aggregato.keys())
    return media

# 3.2 Calcoliamo il consumo medio di ogni valore
def media_vera(diz_consumi: dict) -> float:
    totale = 0
    count = 0
    for lista_consumi in diz_consumi.values():  # Per ogni lista di consumi nel dizionario
        totale += sum(lista_consumi)  # Aggiungiamo al totale la somma della lista
        count += len(lista_consumi)  # Aggiungiamo al divisore della media il numero di elementi di questo mese

    media = totale / count

    # media = sum([sum(consumi) for consumi in diz_consumi.values()]) / sum([len(consumi) for consumi in diz_consumi.values()])
    return media

# Testiamo lo script:
if __name__ == "__main__":
    mese_max = mese_piu_consumo(consumi)
    mese_min = mese_meno_consumo(consumi)
    media_agg = media_aggregato(consumi)
    media_v = media_vera(consumi)
    print(f"Mese con più consumo: {mese_max}")
    print(f"Mese con meno consumo: {mese_min}")
    print(f"Media aggregata: {media_agg:.2f}")
    print(f"media vera: {media_v:.2f}")

