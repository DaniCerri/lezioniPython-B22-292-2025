# Vogliamo salvare e leggere diverse temperature registrate negli ultimi giorni
temperature = [18, 15, 20, 21.2, 16.5, 22, 21.5]  # Salviamo le temperature all'interno di una lista
indice = 3
# Stampiamo una temperatura dalla lista
print(f"Temperatura del giorno {indice}: {temperature[indice]}")

# Calcoliamo la media
totale = temperature[0] + temperature[1] + temperature[2] + temperature[3] + temperature[4] + temperature[5] + temperature[6]
media = totale / 7
print(f"Media: {media:.2f}")