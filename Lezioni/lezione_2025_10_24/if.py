eta = 18  # Età del cliente
orario = (21, 25)  # Orario come ore e minuti

# Se il cliente non ha almeno 18 anni non possiamo dargli alcolici
# Se l'orario supera le 21 non possiamo fornire alcolici a nessuno
if eta >= 18 and orario[0] < 21:
    print("Forniamo alcolici") # Se vero, stampiamo la conferma
else:  # Altrimenti
    if eta < 18: # Diamo "errore"
        print("Sei troppo giovane")
    else:
        print("È troppo tardi per gli alcolici")