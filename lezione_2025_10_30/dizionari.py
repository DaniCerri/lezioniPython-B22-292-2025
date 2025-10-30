# Vogliamo salvarci e calcolare il totale della lista della spesa.
diz_spesa = {
    "Burro": 12.50,
    "Uova": 1.89,
    "Latte": 2.5,
    "Zucchero": 0.99,
    "Farina": 1.3
}

totale = 0
for costo in diz_spesa.values():  # --> diz.values() restituisce una "lista" dei valori del dizionario
    totale += costo

print(f"Costo della spesa: {totale:.2f} €")
totale = sum(diz_spesa.values())  # <-- versione più efficiente

# Stampiamo una lista formattata della nostra spesa
for chiave, valore in diz_spesa.items():
    print(f"  - {chiave}: {valore:.2f} €")

