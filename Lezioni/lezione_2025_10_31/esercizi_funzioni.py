"""
Dato un numero intero > 1 stampare un triangolo di "*" come segue:
es: n = 5
*
**
***
****
*****
"""
def stampa_triangolo(num: int):
    # Stampare il triangolo corrispondente
    for i in range(num):
        print("*" * (i + 1))

"""
Dato un numero intero > 1 e dispari stampare un triangolo di "*" e "+" come segue:
es: n = 5
  *
 ***
*****
  +
"""
def stampa_albero(num: int):
    # Stampare albero di natale
    spostamento = num // 2
    for i in range(num):
        i += 1
        if i % 2 == 1:  # Ci chiediamo se i è dispari
            print(" " * spostamento + "*" * i)
            spostamento -= 1
    print(" " * (num // 2) + "+")

"""
Dato un numero intero, stamapare il quadrato pieno di lato n
e quello vuoto
es: n = 5

*****
*****
*****
*****
*****

*****
*   *
*   *
*   *
*****
"""
def stampa_quadrato(num: int):
    # Quadrato pieno
    for i in range(num):
        print("*" * num)
    print()
    # Quadrato vuoto
    for i in range(num):
        if i == 0 or i == num - 1:
            print("*" * num)
        else:
            print("*" + " " * (num - 2) + "*")

if __name__ == "__main__":
    stampa_quadrato(26)