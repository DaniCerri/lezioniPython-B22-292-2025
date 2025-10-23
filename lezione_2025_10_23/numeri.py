# Calcolo area del triangolo

base = 12  # La base del triangolo è un numero intero
altezza = 10.56  # L'altezza del triangolo è un float

area = base * altezza / 2  # Calcoliamo l'area del triangolo
print(f"L'area del triangolo di base {base} e altezza {altezza} è: {area:.4f}")  # Stampiamo l'area calcolata

# Conversione da secondi a ore
secondi = 7852  # Abbiamo un valore iniziale in secondi
ore = secondi // (60 * 60)  # Calcoliamo quante ore ci sono nei secondi
# secondi -= ore * 3600  # secondi = secondi - ore * 3600 (togliamo i secondi che si possono raggruppare come ore)
secondi = secondi % 3600
minuti = secondi // 60  # Calcoliamo quanti minuti sono rimasti
# secondi -= minuti * 60  # Togliamo i secondi che si possono raggruppare come minuti
secondi %= 60
print(f"Ore: {ore}, Minuti: {minuti}, Secondi: {secondi}")  # Stampiamo il risultato
print(f"{str(ore).zfill(2)}:{str(minuti).zfill(2)}:{str(secondi).zfill(2)}")  # Stampiamo il risultato
# Per ogni variabile, la convertiamo da numero a stringa e poi aggiungiamo a sinistra tanti '0'
# quanti necessari perchè la lunghezza totale sia almeno 2
print('456'.zfill(6))