# Calcoliamo il prezzo totale del necessario per organizzare un evento
num_persone = 45  # Numero di invitati all'evento

# Costi Menu
primo = 12.4  # Costo a testa per il primo
secondo = 17.32  # Costo a testa per il secondo
dolce = 7  # Costo a testa per il dolce
post_dolce = 4  # Costo a testa per il caffè/amaro

affitto = 150  # Costo affitto della sala

# Personale
costo_cameriere = 8  # Costo all'ora di un cameriere
num_camerieri = 7  # Numero di camerieri per l'evento

durata = 4.5  # Durata in ore dell'evento

# 1. Calcoliamo il costo del cibo
costo_menu = primo + secondo + dolce + post_dolce  # Calcoliamo il costo del menu
costo_complessivo_menu = costo_menu * num_persone  # Calcoliamo il costo totale per gli invitati

# 2. Calcoliamo il costo del personale
costo_personale = costo_cameriere * num_camerieri * durata  # Otteniamo il totale moltiplicando i tre valori

# 3. Calcoliamo il costo totale
totale = costo_complessivo_menu + costo_personale + affitto  # Sommiamo tutti i costi per ottenere il totale

# 4. Stampiamo i risultati
print("Costi per l'organizzazione dell'evento: ")
print(f" - Menu: {costo_menu} €/persona -> {costo_complessivo_menu:.2f} €")
print(f" - Personale: {costo_personale} €")
print(f"-" * 70)
print(f"   Totale: {totale:.2f} €")





