# Esercizio: Gestore di Ricette e Dispensa

**Contesto**: Hai una dispensa con ingredienti e vuoi sapere quali ricette puoi cucinare e cosa ti manca.

Dati iniziali:

```python
ricette = {
    "Carbonara": {"pasta", "uova", "guanciale", "pecorino", "pepe"},
    "Pasta al pomodoro": {"pasta", "pomodoro", "basilico", "aglio", "olio"},
    "Tiramisu": {"uova", "mascarpone", "savoiardi", "caffe", "cacao"},
    "Frittata": {"uova", "olio", "sale", "parmigiano"},
    "Aglio e olio": {"pasta", "aglio", "olio", "peperoncino"}
}

dispensa = {"pasta", "uova", "olio", "sale", "aglio", "pepe", "parmigiano"}
```

---

## Esercizio 1
Scrivi un programma che verifichi quali ricette puoi cucinare con gli ingredienti in dispensa e stampi cosa manca per quelle che non puoi preparare.

---

## Esercizio 2
Trova gli ingredienti comuni tra due ricette a tua scelta.

---

## Esercizio 3
Vuoi cucinare "Carbonara" e "Tiramisu". Calcola la lista della spesa completa (ingredienti che ti mancano per entrambe le ricette).

---

## Esercizio 4
Conta quante volte ogni ingrediente appare nelle ricette e stampa i 3 ingredienti più usati.

---

## Esercizio 5
Crea una funzione `lista_spesa_per_ricetta(nome_ricetta, ricette, dispensa)` che stampi cosa devi comprare per preparare una ricetta specifica.

---

## Esercizio 6
Aggiungi 2 nuove ricette al dizionario e verifica se puoi cucinarle con la tua dispensa.

---

## Esercizio 7
Trova tutte le coppie di ricette che NON hanno ingredienti in comune.

---

## Esercizio 8
Crea un dizionario `prezzi` con il costo di ogni ingrediente e calcola quanto costa preparare ogni ricetta. Stampa le ricette ordinate dal costo più basso al più alto.

---

## Esercizio BONUS
Crea un sistema che suggerisca quale ingrediente comprare per sbloccare il maggior numero di ricette.
