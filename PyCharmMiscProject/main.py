from random import random

print("ciao")  #Sistema di print in Python


def saluta():
    print("Hello World!")


saluta()  #un blocco di codice

print("--------------------------------------------------------------------------------------------")

a = 5
b = 15
c = 20

print(a + b)  #somma
print(a - b)  #sottarzione
print(a / b)  #divisione
print(a % b)  #resto della divisione
print(a ** 2)  #elevamento alla potenza
print(a // 3)  #divisione intera

print("--------------------------------------------------------------------------------------------")

#operatori di confronto con ris: True o False
print(a == b)  #i 2 valori sono uguali
print(a != b)  #verifica se le 2 varibaili siano uguali
print(a > b)  #verifica se la variabile "a" sia maggiore della varibile "b"
print(a < b)  #verifica se la variabile "a" sia minore della varibile "b"
print(a >= b)  #se la variabile "a" è maggiore o uguale della variabile "b"
print(a <= b)  #se la variabile "a" è minore o uguale della variabile "b"

print("--------------------------------------------------------------------------------------------")

#operatori logici: and, or, not
print(a < b and b < c)  #and
print(a < b or b < c)  #or
print(not a < b)  #not

print("--------------------------------------------------------------------------------------------")

#strutture di controllo: if-else statement, while loop, for loop
#while loop
x = 0

while x < a:
    print(x)
    x += 1
print("---------FINE  PRIMO ESEMPIO DI TIPO CICLO--------------------------------------------------")
#for loop
frutta = ["fragola", "banana", "kiwi"]
for frutta in frutta:
    print(frutta)

print("---------FINE  SECONDO ESEMPIO DI TIPO CICLO------------------------------------------------")
#if-else statement
y = 11

if y > 10:
    print("Maggiore!")
else:
    print("Minore!")

print("---------FINE  TERZO ESEMPIO DI TIPO CICLO--------------------------------------------------")


def calcola_area(base, altezza):
    area = base * altezza
    return area


#Chiamata alla funzione passando gli argomenti posizionalmente
risultato1 = calcola_area(5, 10)
print(risultato1)

#ADESSO ABBIAMO GIU' UN'ALTRO METODO

#Chimata alla funzione specificando esplcitamente i nomi dei parametri
risultato2 = calcola_area(base=100, altezza=50)
print(risultato2)

print("---------ISTRUZIONE PASS-----------------------------------------------------------------")


def mia_funzione():
    pass
