# exercice-07-boucles.py

import random

# exo 7.1
# en utilisant une boucle for, affichez les nombre de 0 à 99 inclus

# réponse 7.1
for i in range(100):
    print(i)
# exo 7.2
# en utilisant une boucle for, affichez les nombre de 0 à 100 inclus

# réponse 7.2
for i in range (101):
    print (i)
# code 7.1
# affectation d'un nombre aléatoire compris entre 1 et 10 inclus
number = random.randint(1, 10)

# exo 7.3
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1

# réponse 7.3
for games in range (100):
    games +=1
    r = number
    if r == 1:
        print(r)
# exo 7.4
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus petit ou égal à 5

# réponse 7.4
for games in range (50):
    games +=1
    r =number
    if r <=5:
        print(' le résultat est plus petit que 5: ' + str(r))
# exo 7.5
# en utilisant une boucle for, on tire 20 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus grand ou égal à 6

# réponse 7.5
for games in range (20):
    games += 1
    r =number
    if r >=6:
        print (r)
# exo 7.6
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1 ou égal à 10

# réponse 7.6
for games in range(100):
    games +=1
    r = number
    if r == 1 or r == 10:
        print(r)
    # exo 7.7
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est compris entre 3 et 8 inclus

# réponse 7.7
for r in range (10):
    if 3 <number <=8:
        print(r)
# exo 7.8
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est égal à 7
# affichez la variable `count`

# réponse 7.8
for r in range (50):
    count  = r
    if r == 7:
        count +=1
        print(count)
    # exo 7.9
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 4
# affichez la variable `count`

# réponse 7.9
r  = random.randint(0, 10)
for r in range(66):
    
    if r <= 4:
        count = r + 1
        print(count)

# exo 7.10
# en utilisant une boucle for, on tire 33 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus grand ou égal à 7
# affichez la variable `count`

# réponse 7.10
r = random.randint(0, 11)
for r in range(33):
    if r <= 7 :
        count = r + 1
        print(count)
# exo 7.11
# en utilisant une boucle for, on tire 66 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 2, ou plus grand ou égal à 9
# affichez la variable `count`

# réponse 7.11
for r in range(66):
    if r <=2 or r >=9:
        count = r + 1
        print(count)
# exo 7.12
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est compris entre 2 et 9 inclus
# affichez la variable `count`

# réponse 7.12
for r in range (0, 100):
    count = r +1
    if 2 < r < 9:
        print(count)
# exo 7.13
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 99 inclus

# réponse 7.13
for r in range (1, 100):
    if r %  2 ==0:
        print(i)
# exo 7.14
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 100 inclus

# réponse 7.14
for i in range(101):
    if i % 2 == 0:
        print(i)
# exo 7.15
# en utilisant une boucle for, affichez tous les nombres divisibles par 3, de 2 à 99 inclus

# réponse 7.15
for i in range (2, 100):
    if i % 3 == 0:
        print(i)
# code 7.2
# pour calculer la puissance 2 d'un nombre, on peut le multiplier par lui-même
number = random.randint(3, 10)
print(number * number)
# mais on peut aussi l'élever à la puissance 2 avec l'opérateur puissance `**`
print(number ** 2)

# exo 7.16
# en utilisant une boucle for, affichez la puissance 2 des nombres de 0 à 99 inclus
for i in range(number):
    print(i ** 2)
# réponse 7.16

# code 7.3
# pour calculer la puissance 3 d'un nombre, on peut l'élever à la puissance 3 avec l'opérateur puissance `**`
number = random.randint(3, 10)
print(number ** 3)

# exo 7.17
# en utilisant une boucle for, affichez la puissance 3 des nombres de 1 à 100 inclus

# réponse 7.17
for i in range(100):
    print(i ** 3)
# exo 7.18
# dans une boucle while, on tire un nombre entier `r` au hasard entre 1 et 100 inclus
# boucler jusqu'à ce que la valeur 100 soit tirée au hasard

# réponse 7.18
i = random.randint(0, 101)
while i < 100:
    print(i)
    break