# Esercizio: Sistema di Gestione Centro Sportivo

## Problema

Il centro sportivo "FitLife" offre diversi corsi fitness e vuole analizzare la partecipazione degli iscritti per ottimizzare l'offerta. Il centro tiene traccia del numero di partecipanti per ogni corso in diverse fasce orarie durante la settimana.

Il centro offre 5 corsi: **Yoga**, **Pilates**, **Spinning**, **CrossFit** e **Zumba**.

Ogni corso ha 3 fasce orarie disponibili: **Mattina (9:00)**, **Pomeriggio (14:00)** e **Sera (19:00)**.

### Dati partecipanti per fascia oraria (ultimi 5 giorni lavorativi)

**Yoga:**
- Mattina: 12, 15, 13, 14, 16
- Pomeriggio: 8, 9, 7, 10, 9
- Sera: 18, 20, 19, 21, 22

**Pilates:**
- Mattina: 10, 11, 9, 12, 10
- Pomeriggio: 15, 14, 16, 15, 17
- Sera: 20, 22, 21, 23, 24

**Spinning:**
- Mattina: 8, 9, 7, 8, 10
- Pomeriggio: 12, 14, 13, 15, 14
- Sera: 25, 28, 26, 27, 29

**CrossFit:**
- Mattina: 14, 16, 15, 17, 16
- Pomeriggio: 18, 19, 17, 20, 19
- Sera: 22, 24, 23, 25, 26

**Zumba:**
- Mattina: 6, 7, 5, 8, 7
- Pomeriggio: 20, 22, 21, 23, 22
- Sera: 16, 18, 17, 19, 18

## Richieste

Crea un programma che:

1. Memorizzi questi dati in una struttura appropriata (dizionario che per ogni corso contenga un sotto-dizionario con le tre fasce orarie, ognuna con la propria lista di partecipanti)

2. Implementa una funzione `media_partecipanti(corso, fascia_oraria)` che calcola la media dei partecipanti per un corso specifico in una fascia oraria specifica

3. Implementa una funzione `fascia_piu_frequentata(corso)` che restituisce il nome della fascia oraria più frequentata per quel corso (basandosi sulla media)

4. Implementa una funzione `corso_piu_popolare()` che restituisce il nome del corso con il maggior numero totale di partecipanti (sommando tutte le fasce orarie e tutti i giorni)

5. Implementa una funzione `giorno_migliore(corso, fascia_oraria)` che restituisce il giorno (posizione 0-4) con più partecipanti per quella combinazione corso-fascia

6. Implementa una funzione `analisi_completa()` che stampa un report con:
   - Il corso più popolare in assoluto
   - Per ogni corso, quale fascia oraria è più frequentata
   - La media generale di partecipanti per ogni fascia oraria (considerando tutti i corsi)

## Obiettivo

Testa il programma generando l'analisi completa e rispondi alle seguenti domande:
- Quale corso dovrebbe avere più istruttori disponibili?
- Quali fasce orarie sono generalmente meno frequentate e potrebbero essere eliminate o modificate?
- C'è un trend crescente o decrescente nelle partecipazioni durante la settimana?
