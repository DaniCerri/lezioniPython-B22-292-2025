"""
Abbiamo un dizionario con una serie di liste di numeri, vogliamo per ognuna
calcolarne le statistiche (media, std_dev, massimo)
"""
import qualche_funzione


def report(dizionario_record: dict) -> str:
    """
    Funzione che calcola un report completo delle statistiche di un record
    :param dizionario_record: {"nome": str, "lista": list[int]
    :return: str con report completo
    """
    # Per chiamare una funzione di un altro file, utilizziamo la sintassi
    # nome_file.nome_funzione(parametri)
    media = qualche_funzione.calc_media(dizionario_record['valori'])
    std_dev = qualche_funzione.calc_std_dev(dizionario_record['valori'])
    massimo = qualche_funzione.calc_massimo(dizionario_record['valori'])
    separatore = qualche_funzione.separatore(50, "-", dizionario_record['nome'])

    stringa_out = f"{separatore} \n"
    stringa_out += f"Media: {media:.2f} \n"  # Il \n serve per andare a capo
    stringa_out += f"Std Dev: {std_dev:.2f} \n"  # Il \n serve per andare a capo
    stringa_out += f"Massimo: {massimo:.2f} \n"  # Il \n serve per andare a capo

    return stringa_out

dati = [
    {
        "nome": "Temperature",
        "valori": [18, 22, 25, 23, 20, 19]
    },
    {
        "nome": "Vendite",
        "valori": [150, 200, 180, 220, 195, 210]
    },
    {
        "nome": "Utenti",
        "valori": [1200, 1350, 1500, 1420, 1600, 1580]
    }
]

for record in dati:  # Per ogni record del nostro dizionario
    report_dato = report(record)  # Facciamo un report completo
    print(report_dato)