separatore = "-" * 50

# Calcoliamo il consumo medio al km di un viaggio [L/km]
print(f"{separatore} Consumo medio {separatore}")
km = 123  # km percorsi [km]
prezzo_benzina = 1.7  # Prezzo della benzina al litro [€/L]
costo_benzina = 45.53  # Soldi spesi in benzina per il viaggio [€]

litri_benzina = costo_benzina / prezzo_benzina  # Calcoliamo i litri utilizzati [L]
consumo = litri_benzina / km  # Calcoliamo il consumo [L/km]

print(f"Consumo: {consumo:.4f} L/km")
print(f"Consumo: {1/consumo:.4f} km/L")
print(separatore*2)

# Calcoliamo (in maniera inefficiente) la media delle temperature degli ultimi 5 giorni
print(f"{separatore} Temperatura media {separatore}")
totale = 25 + 24 + 23.7 + 29 + 18
media = totale / 5
print(f"Temperatura media: {media:.2f} °C")
print(separatore * 2)

# Calcoliamo l'area del cerchio dato il diametro
print(f"{separatore} Cerchio {separatore}")
diametro = 78.1254
area = (diametro / 2) ** 2 * 3.14
print(f"Area del cerchio: {area:.4f}")
print(separatore * 2)

# Calcoliamo (in maniera inefficiente) quanto deve pagare ogni coinquilino delle bollette
print(f"{separatore} Affitto {separatore}")
coeff_giulia = 360 # /365
coeff_ilaria = 280 # /365
coeff_luca = 325 # /365
totale_affitto = 450 * 12
totale_riscaldamento = 82.16 * 12
totale_bollette = 146.45 * 12

totale = totale_affitto + totale_riscaldamento + totale_bollette
totale_giorni_in_casa = coeff_giulia + coeff_ilaria + coeff_luca

speso_giulia = (coeff_giulia / totale_giorni_in_casa) * totale
speso_ilaria = (coeff_ilaria * totale) / totale_giorni_in_casa
speso_luca = (coeff_luca * totale) / totale_giorni_in_casa
print(f"Giulia ha speso: {speso_giulia:.2f} €")
print(f"Ilaria ha speso: {speso_ilaria:.2f} €")
print(f"Luca ha speso: {speso_luca:.2f} €")
# print(totale_giorni_in_casa)
# print(speso_luca + speso_ilaria + speso_giulia)
# print(totale)
print(separatore * 2)


