# Le funzioni sono dei sottoprogrammi che ci consentono di riutilizzare dei blocchi di codice

# Dichiaramo una funzione con la keyword "def"
def nome_funzione(parametro1, parametro2):
    something = ...
    # codice della funzione
    ...
    return something  # <- Opzionale, serve per fare uscire i valori dalle funzioni

def calc_bmi(altezza: float, peso: float) -> float:
    """
    Calcola Body Mass Index da altezza (in metri) e peso (in kg)
    :param altezza: Altezza in metri
    :param peso: Peso in kg
    :return: bmi, float
    """
    bmi = round(peso / (altezza ** 2), 4)
    return bmi

dizionario_persone = {
    "Daniele": {"eta": 21, "altezza": 1.75, "peso": 61.3},
    "Luca": {"eta": 46, "altezza": 1.80, "peso": 76.2},
    "Ilaria": {"eta": 12, "altezza": 1.67, "peso": 50.2},
    "Federica": {"eta": 25, "altezza": 1.58, "peso": 68.4},
    "Mattia": {"eta": 78, "altezza": 1.91, "peso": 98.3},
}

# Vogliamo calcolare la BMI di una persona
# BMI = peso / (altezza in metri) ** 2
for persona, dati in dizionario_persone.items():
    BMI = calc_bmi(dati['altezza'], dati['peso'])
    print(f"La BMI di {persona} è {BMI}")

# Sappiamo che la BMI corretta corrisponde a una persona alta 1.75 che pesa 60 kg
# Avendo fatto la funzione possiamo calcolarla facilmente in modo da confrontare ogni persona
bmi_riferimento = calc_bmi(1.75, 60)
print(f"La BMI di riferimento è {bmi_riferimento}")

# Regole importanti
# Una funzione deve fare solo un task e deve essere "corta"
# Le librerie sono collezioni di funzioni, ognuna chiamabile e utilizzabile a sè
# Per utilizzare una libreria la importiamo con "import" -> All'inizio del file