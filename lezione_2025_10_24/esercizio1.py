# Calcoliamo le spese che devono affrontare 3 coinquilini
affitto_mensile = 450  # Costo dell'affitto dell'appartamento

# Costo del riscaldamento da Gennaio [0] a Dicembre [11]
costi_riscaldamento = [120, 114.2, 78.45, 50.23, 20.1, 0, 0, 0, 0, 48.2, 60, 145.2]

# Costo delle bollette da Gennaio [0] a Dicembre [11]
costi_bollette = [45.3, 156.3, 160.1, 89.23, 69.32, 145.3, 20.6, 45.2, 123.01, 147.25, 187.1, 56.2]

# Coeff di spesa
coeff_ilaria = 280/365  # Giorni in cui Ilaria è stata a casa su 365
coeff_giulia = 360/365  # Giorni in cui Giulia è stata a casa su 365
coeff_luca = 320/365  # Giorni in cui Luca è stato a casa su 365

# Calcoliamo il totale annuo del riscaldamento
costo_totale_riscaldamento = 0
for elem in costi_riscaldamento:
    costo_totale_riscaldamento += elem

# Calcoliamo il totale annuo delle bollette
costo_totale_bollette = 0
for bolletta in costi_bollette:
    costo_totale_bollette += bolletta

totale_coeff = coeff_giulia + coeff_ilaria + coeff_luca  # Calcoliamo il totale dei coefficienti per la divisione

# Calcoliamo il totale di tutte le spese
totale_complessivo = affitto_mensile * 12 + costo_totale_bollette + costo_totale_riscaldamento

# Calcoliamo per ogni inquilino quanto paga
speso_giulia = coeff_giulia / totale_coeff * totale_complessivo
speso_ilaria = coeff_ilaria / totale_coeff * totale_complessivo
speso_luca = coeff_luca / totale_coeff * totale_complessivo

# print dei risultati
print(f"Giulia ha speso: {speso_giulia:.2f} €")
print(f"Ilaria ha speso: {speso_ilaria:.2f} €")
print(f"Luca ha speso: {speso_luca:.2f} €")

# Esercizio per il weekend:
# Adattare lo script in modo che funzioni con un elenco di coinquilini (nome, coeff)





# Suggerimento: Sarebbe comodo iterare tra i coinquilini per i vari calcoli che li riguardano
















# Suggerimento 2: provate a fare una lista con i coinquilini
