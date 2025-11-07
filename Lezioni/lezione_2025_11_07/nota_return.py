# 1. Esempio senza return
def molt_no_return(p: int, q: int) -> None:
    for i in range(p):
        for j in range(q):
            print(f"{i} * {j} = {i * j}")

def molt_return_1(p: int, q: int) -> int:
    for i in range(p):
        for j in range(q):
            print(f"{i} * {j} = {i * j}")

    return i * j

def molt_return_2(p: int, q: int) -> int:
    for i in range(p):
        for j in range(q):
            print(f"{i} * {j} = {i * j}")

        return i * j

def molt_return_3(p: int, q: int) -> int:
    for i in range(p):
        for j in range(q):
            print(f"{i} * {j} = {i * j}")

            return i * j
    return -1


# Esempio di utilizzo del return per interrompere una funzione
# Dobbiamo trovare la posizione (se c'è) del numero 3 nella lista
def trova_3(lista: list[int]) -> int:
    for i in range(len(lista)):
        print(f"Esamino l'elemento a posizione {i}")
        if lista[i] == 3:
            print(f"Ho trovato il 3 alla posizione {i}")
            return i

    # Se non lo troviamo, restituiamo il codice -1
    print("Il 3 non è nella lista")
    return -1

if __name__ == "__main__":
    molt_no_return(5, 6)
    print(f"Sono il print del main 1: {molt_return_1(5, 6)}")
    print(f"Sono il print del main 2: {molt_return_2(5, 6)}")
    print(f"Sono il print del main 3: {molt_return_3(5, 6)}")
    lista1 = [15, 21, 8, 4, 35, 88, 25, 2, 91]
    lista2 = [15, 21, 8, 4, 35, 3, 25, 2, 91]

    print(f"Posizione del 3 in {lista1}: {trova_3(lista1)}")
    print(f"Posizione del 3 in {lista2}: {trova_3(lista2)}")
