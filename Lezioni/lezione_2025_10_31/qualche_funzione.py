# La funzione calc_media prende in input una lista di numeri interi
# e restituisce la media come float

def calc_media(lista: list[int]) -> float:
    """
    La funzione calc_media prende in input una lista di numeri interi e restituisce la media come float
    :param lista: Lista di numeri interi
    :return: Media, float
    """
    media = sum(lista) / len(lista)
    return media

def separatore(lunghezza: int, carattere: str, titolo: str):
    output = carattere * (lunghezza // 2)
    output += f" {titolo} "
    output += carattere * (lunghezza // 2)
    return output

def calc_std_dev(lista: list[int]) -> float:
    """
    Calcola la deviazione standard di una lista di interi
    :param lista: Lista di numeri interi
    :return: std_dev, float
    """
    media = calc_media(lista)  # Calcoliamo la media con la funzione che abbiamo fatto prima
    tot = 0
    for numero in lista:
        tot += (numero - media) ** 2
    varianza = tot / len(lista)
    std_dev = varianza ** 0.5
    # Facciamo uscire dalla funzione (che altrimenti vediamo come una scatola chiusa)
    # il valore calcolato per la deviazione standard -> con il return
    return std_dev

def calc_massimo(lista: list[int]) -> int:
    """
    Trova il massimo della lista
    :param lista: Lista di numeri interi
    :return: massimo, int
    """
    massimo = lista[0]
    for numero in lista:
        if massimo < numero:
            massimo = numero

    return massimo

# Una cosa molto importante quando si utilizzano le funzioni è inserire il codice di test o
# del programma in corso sotto un if __name__ == "__main__"
# In questo modo, il codice di test viene eseguito SOLAMENTE se viene chiamato direttamente lo script
# -> Quindi se importiamo il file in un altro script, il codice di test non viene eseguito

if __name__ == "__main__":
    lista_numeri = [43, 4, 65, 8, 23, 12, 456, 47, 78, 21]
    print(f"La media della lista è {calc_media(lista_numeri):.2f}")

    lista_due = [69, 61, 121, 45, 6, 78, 42]
    print(f"La media della lista nuova è {calc_media(lista_due):.2f}")

    separatore(50, "-", "Separatore")

