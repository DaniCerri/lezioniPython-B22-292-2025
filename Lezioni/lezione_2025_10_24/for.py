temperature = [12, 11.5, 12, 16, 17.2, 21, 20, 16.4, 15.3]  # Creiamo la lista di temperature
n = len(temperature)  # Otteniamo la lunghezza della lista
tot = 0  # Inizializziamo il totale a 0

for i in range(n):
    e = temperature[i]  # Otteniamo l'elemento alla posizione i
    tot += e  # Aggiungiamo al totale il valore appena ottenuto (tot = tot + e)

media = tot / n
print(f"La temperatura media è: {media:.2f} °C")


# Variante più "Python-iana"
tot = 0  # Ri-azzeriamo il totale
for temperatura in temperature:  # Per ogni temperatura in temperature
    tot += temperatura  # Aggiungiamo la temperatura al totale
media = tot / n
print(f"La temperatura media è: {media:.2f} °C")

