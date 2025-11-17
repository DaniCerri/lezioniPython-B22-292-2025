# Errori Comuni e Criticità Riscontrate

## Python

**Errori critici:**
- Funzioni incomplete o non inizializzate: alcuni di voi hanno dimenticato di inizializzare variabili (es. `frequenze = {}`, `duplicati = []`)
- Mancata gestione liste vuote: ricordatevi sempre di controllare il caso `if not lista` per evitare `ZeroDivisionError`
- Errori di indentazione: il `return` deve essere FUORI dal ciclo `for`, non dentro

**Errori logici:**
- Confronto `numero == lista[i]` invece di confrontare con altri elementi
- Uso di `//` (divisione intera) invece di `/` per calcolare medie
- Restituzione di liste invece di dizionari quando richiesto

**Cosa manca:**
- Arrotondamento con `round(media, 2)`
- Commenti e docstring: solo pochi hanno commentato adeguatamente

## JavaScript

**Errori di sintassi:**
- Typo frequente: `array.lenght` invece di `array.length`
- Punto e virgola dopo `if` che crea blocchi vuoti: `if (array.length === 0);`
- Codice irraggiungibile dopo `return`

## HTML

**Errore principale:**
- Liste mal strutturate: molti hanno usato tre `<ul>` separati invece di un unico `<ul>` con tre `<li>`
- Uso di tag non standard: `<p1>`, `<p2>`, `<p3>` non esistono in HTML
- Link CSS nel `<body>` invece che nel `<head>`

**Problemi strutturali:**
- Due strutture HTML complete nello stesso file
- CSS inline invece di collegamento esterno

## CSS

**Errori frequenti:**
- Margin/padding applicati su `<ul>` invece che su `<li>`
- Valori errati: `5px` invece di `10px`, `20px` invece di `18px`
- Errori sintattici: spazi nelle unità (`10 px` invece di `10px`)
- Duplicazione: CSS sia inline che in file separato

**Mancanze:**
- Unità di misura omesse: `10` invece di `10px`
- Nessun commento esplicativo

## SQL

**Errori critici:**
- `CREATE TABLE` completamente mancante in alcuni casi
- Query `SELECT` posizionata PRIMA degli `INSERT` (ordine logico errato)

**Errori di sintassi:**
- Virgole invece di punti per decimali: `2,25` invece di `2.25`
- Punto e virgola posizionato male

**Mancanze:**
- Pochi commenti esplicativi

## Osservazioni Generali

**Punti di forza:**
- Tutti avete dimostrato impegno e comprensione di base
- Nonstante il poco tempo avete generalmente valorizzato le differenze dei linguaggi, ben eseguiti nella struttura base

**Cosa migliorare:**
- Attenzione ai dettagli: ricontrollate indentazione, sintassi, nomi variabili
- Testate il codice prima di consegnare
- Commentate SEMPRE: vi aiuta a ragionare e vale punti bonus
- Gestite i casi limite (liste vuote, array vuoti, ecc.)

# Ultimo consiglio
Molti di voi hanno saltato delle funzioni senza scrivere nulla, vi consiglio per le prove future di provare comunque a scrivere qualcosa, pochi punti (eventuali) sono meglio di nessuno.
