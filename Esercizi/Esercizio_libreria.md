# Esercizio: Gestione Inventario Libreria

## Problema

La libreria "Pagine Felici" deve organizzare il proprio inventario digitale. Il proprietario vuole un sistema che tenga traccia di diversi generi letterari e, per ogni genere, memorizzare il numero di copie disponibili per ciascun mese dell'anno.

La libreria gestisce 4 generi principali: **Gialli**, **Romanzi**, **Fantascienza** e **Saggistica**.

### Dati delle vendite (ultimi 6 mesi)

- **Gialli**: 45, 52, 38, 61, 49, 55
- **Romanzi**: 78, 82, 91, 88, 76, 85
- **Fantascienza**: 23, 28, 31, 26, 29, 34
- **Saggistica**: 15, 18, 22, 19, 17, 21

## Richieste

Crea un programma che:

1. Memorizzi questi dati in una struttura appropriata (dizionario contenente per ogni genere il nome e la lista delle vendite)

2. Implementa una funzione `calcola_media_vendite(genere)` che restituisce la media delle vendite per quel genere

3. Implementa una funzione `genere_piu_venduto()` che restituisce il nome del genere con il maggior numero di vendite totali

4. Implementa una funzione `mese_migliore(genere)` che restituisce il mese (posizione nella lista) in cui quel genere ha venduto di più

## Obiettivo

Testa il programma calcolando quale genere ha performato meglio e qual è stata la media di vendite per ogni categoria.
