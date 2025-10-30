BUDGET = 50  # Definiamo il nostro budget da rispettare
lista_spesa = [
    ("Pane", 2.50),
    ("Latte", 1.80),
    ("Pasta", 1.20),
    ("Pomodori", 3.50),
    ("Formaggio", 5.00),
    ("Biscotti", 3.80),
    ("Mele", 2.90),
    ("Olio", 6.50),
    ("Riso", 2.00),
]  # Inizializziamo la lista della spesa

# 1. Quanto spenderesti se comprassi tutti i prodotti della lista?
totale = 0  # Inizializziamo il totale a 0
for item in lista_spesa:  # Per ogni item nella nostra lista
    # Prendiamo il costo (alla posizione 1 della tupla) e lo aggiungiamo al totale
    totale += item[1]  # -> totale = totale + item[1]

print(f"Totale spesa: {totale:.2f}")

# 2. Il totale della spesa supera il tuo budget di 50 euro? Di quanto?
differenza = BUDGET - totale  # Calcoliamo la differenza tra budget e totale
# Controlliamo la differenza con il budget
if differenza >= 0: # Se è >= 0 -> Sono bastati i soldi
    print(f"Non sforiamo il budget: avanzano {differenza:.2f} €")
else: # Altrimenti ne servono di più
    print(f"Abbiamo sforato il budget: ci sono {-differenza:.2f} € di troppo")

# 3. Se decidessi di aggiungere i prodotti al carrello uno alla volta
# (nell'ordine della lista), quali prodotti riusciresti a comprare senza superare
# il budget? Mostra il totale parziale dopo ogni prodotto aggiunto.
totale = 0
elementi_presi = []
for item in lista_spesa:
    totale_tmp = totale + item[1]  # Calcoliamo un totale temporaneo
    # --> Calcoliamo quanto sarebbe il totale se comprassimo anche l'elemento corrente
    print(f"Totale fin'ora: {totale_tmp}, aggiungerei '{item[0]}'")
    # Se non staremmo sforando il budget, ufficializziamo l'acquisto
    if totale_tmp <= BUDGET:
        totale += item[1]  # Aggiungiamo il costo al totale ufficiale
        elementi_presi.append(item)  # Salviamo l'elemento in quelli presi

print(f"Acquistati: {elementi_presi}")