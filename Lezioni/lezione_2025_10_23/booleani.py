# Facciamo 3 variabili booleane che sono piove, ritardo, sciopero.
# Le mettiamo insieme in almeno 3 modi per creare tre "politiche" di scelta per prendere o no la macchina
piove = False  # False
ritardo = True
sciopero = False

politica1 = (piove and sciopero) or ritardo
politica2 = (ritardo or piove) and not sciopero
politica3 = not (ritardo and piove) or not sciopero

print(f"Politica1: {politica1}")
print(f"Politica2: {politica2}")
print(f"Politica3: {politica3}")
